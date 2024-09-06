# Image to Video Creator

This repository contains a Python script that converts a stream of ROS image messages into a video file. The script subscribes to a specified ROS image topic, converts the images to OpenCV format, and writes them to a video file. The video files are created with a specified duration and saved in a designated output directory.


## Usage

A Dockerfile is provided to create a Docker image with all necessary dependencies.

At the same time, a shell script is provided to run the container with the necessary arguments.

```sh:run_video_creator.sh
./run_video_creator.sh [video_duration_seconds]
```


- `video_duration_seconds` (optional): The duration of each video file in seconds. Defaults to 30 seconds if not provided.


## Output

The video files are now saved in the `~/Videos/ros_videos` directory in the host machine. You can change this in the `video_creator.py` file.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
