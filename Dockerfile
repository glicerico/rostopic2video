# Use an official ROS base image
FROM ros:noetic-ros-base

# Install dependencies for ROS and OpenCV
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-opencv \
    ros-noetic-cv-bridge \
    ros-noetic-rospy && \
    rm -rf /var/lib/apt/lists/*

# Set up your working directory
WORKDIR /app

# Copy the Python script and entrypoint script into the container
COPY video_creator.py /app/video_creator.py
COPY entrypoint.sh /app/entrypoint.sh

# Source ROS environment
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the script
ENTRYPOINT ["/app/entrypoint.sh"]
