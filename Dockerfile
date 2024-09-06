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

# Copy the Python script into the container
COPY video_creator.py /app/video_creator.py

# Source ROS environment
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Set the command to run your Python script
CMD ["python3", "/app/video_creator.py"]
