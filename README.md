# ROS2 Template

## Init ROS2 Middleware

```bash
source /opt/ros/humble/setup.bash
```

## Create ROS2 Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
sudo rosdep install -i --from-path src --rosdistro humble -y
```

## Create ROS2 Package

```bash
pwd # ~/ros2_ws
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python sample
```

## Build ROS2 Package

```bash
pwd # ~/ros2_ws
colcon build --symlink-install
# or 
# colcon build --symlink-install

# you can select the package to build
# colcon build --packages-select sample
```
