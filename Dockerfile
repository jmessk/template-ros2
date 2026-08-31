ARG ROS_DISTRO=jazzy


FROM ros:${ROS_DISTRO}-ros-base AS build

ARG ROS_DISTRO
ARG PACKAGE_NAME

COPY src /workspace/src
WORKDIR /workspace
RUN test -n "${PACKAGE_NAME}" \
    && /bin/bash -c \
        "source /opt/ros/${ROS_DISTRO}/setup.bash \
        && colcon build --packages-up-to ${PACKAGE_NAME}"


FROM ros:${ROS_DISTRO}-ros-core AS example_talker

COPY --from=build /workspace/install /workspace/install
WORKDIR /workspace
USER ubuntu


FROM ros:${ROS_DISTRO}-ros-core AS example_listener

COPY --from=build /workspace/install /workspace/install
WORKDIR /workspace
USER ubuntu
