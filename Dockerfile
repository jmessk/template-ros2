FROM ros:humble

RUN mkdir -p /root/ros2_ws/src

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
