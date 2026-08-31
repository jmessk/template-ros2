ARG ROS_DISTRO=jazzy


FROM ros:${ROS_DISTRO}-ros-base

WORKDIR /workspace
USER ubuntu
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

CMD ["sleep", "infinity"]
