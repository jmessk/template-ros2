FROM ros:humble

ARG UID
ARG GID

RUN groupadd -g ${GID} user && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} user

RUN echo "source /opt/ros/humble/setup.bash" >> /home/user/.bashrc
USER user
RUN mkdir -p /home/user/ros2_ws/src
WORKDIR /home/user/
