FROM ros:humble

ARG UID
ARG GIO

RUN groupadd -g $GID user && \
    useradd -m -s /bin/bash -u $UID -g $GID user

RUN apt-get update && apt-get install -y \
    python3-pip

RUN echo "source /opt/ros/humble/setup.bash" >> /home/user/.bashrc
USER ${UID}
WORKDIR /home/user/ros2_ws/
