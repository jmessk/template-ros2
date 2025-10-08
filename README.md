# ROS2 Template

## Getting Started

You can set up a ROS2 development environment by following the steps below.

1. **Start the development container**

    ```bash
    docker compose up -d
    ```

2. **Access the container (bash)**

    If you did not use `-d` option in step 1, run this in other terminal.

    ```bash
    docker compose exec dev bash
    ```

3. **(optional) Run example**

    publisher:

    ```bash
    cd ~/ros2_ws
    colcon build
    source install/setup.bash

    ros2 run examples pub
    ```

    subscriber:

    Please run in another terminal.

    ```bash
    source install/setup.bash
    ros2 run examples sub
    ```

## Configuration

- `compose.yml`

  - **`UID` and `GID` in build args**: To avoid permission issues with files and directories, it is recommended to set the user inside the container to have the same user ID and group ID as the host.

  - **`ROS_DOMAIN_ID` in environment variables**: Set this to your desired ROS2 domain ID.

  - **GUI**: To enable GUI applications, `/tmp/.X11-unix` is mounted and `DISPLAY` environment variable is set. You may need to allow the container to access your X server by running `xhost +local` on the host.

  To show GUI apps over SSH (with X11 forwarding), also mount your Xauthority file (`~/.Xauthority`) to the container. This allows GUI applications inside the container to connect to your forwarded X server. Use options `ssh -X` or `ssh -Y`.

  - **Devices**: Map host device nodes to access hardware from the container. Example: `/dev/video0:/dev/video0` for a webcam. Ensure your user has permission for the device (e.g., belongs to the `video` group).

  - **mDNS**: If you want to use mDNS (`*.local:`), `/var/run/dbus` and `/var/run/avahi-daemon/socket` are mounted. Make sure that the Avahi daemon is running on the host.
