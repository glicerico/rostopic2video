import cv2
import rospy
import signal
import sys
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# Initialize the ROS node
rospy.init_node('image_to_video')

# Set up the OpenCV bridge to convert ROS image messages to OpenCV images
bridge = CvBridge()

# Variables to manage the video recording
frame_width, frame_height = 640, 480  # Modify these values based on your images
fps = 30  # Frames per second
video_output_directory = "/app/output"
video_filename_template = video_output_directory + "/video_{}.avi"

# Time-based control variables
video_duration_seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 30  # Default to 30 seconds if not provided
last_time = time.time()
video_index = 0  # Track the number of videos created

# Function to start a new video
def start_new_video():
    global out, video_index, last_time
    if 'out' in globals():
        out.release()  # Release the current video file if it exists
        rospy.loginfo(f"Video {video_index} saved.")
    video_index += 1
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    video_output_path = video_filename_template.format(timestamp)
    out = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
    last_time = time.time()
    rospy.loginfo(f"Started new video: {video_output_path}")

# Start the first video
start_new_video()

def image_callback(msg):
    try:
        global last_time
        # Convert ROS Image message to OpenCV image
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        
        # Write the frame to the video
        out.write(cv_image)
        
        # Log that a frame is being written (optional, comment out if too verbose)
        rospy.loginfo(f"Frame written to video {video_index}")
        
        # Check if the specified duration has passed, and if so, start a new video
        if time.time() - last_time >= video_duration_seconds:
            start_new_video()

    except Exception as e:
        rospy.logerr("Failed to convert image: %s" % str(e))

# Graceful shutdown handler
def signal_handler(sig, frame):
    rospy.loginfo("Stopping recording...")
    if 'out' in globals():
        out.release()  # Release the video writer
        rospy.loginfo(f"Final video {video_index} saved.")
    sys.exit(0)

# Register the signal handler for SIGINT (CTRL+C) and SIGTERM
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Subscribe to the ROS image topic (choose the one you need)
# image_topic = '/hr/sensors/vision/chest_cam/chest_usb_cam/image_raw'  # Topic from the realsense camera
image_topic = '/hr/perception/ui_image'  # Topic from the webUI image
rospy.Subscriber(image_topic, Image, image_callback)

# Keep the node running until manually stopped
rospy.spin()
