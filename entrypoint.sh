#!/bin/bash

# Source ROS environment
source /opt/ros/noetic/setup.bash

# Run the Python script with any passed arguments
exec python3 /app/video_creator.py "$@"