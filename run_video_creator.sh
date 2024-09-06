#!/bin/bash

# Create the output directory if it doesn't exist
mkdir -p ~/Videos/ros_videos

# Set default video duration
VIDEO_DURATION=${1:-30}

# Build the Docker image
docker build -t video_creator .

# Run the Docker container with the video duration argument
docker run -it -v ~/Videos/ros_videos:/app/output --network="host" video_creator $VIDEO_DURATION
