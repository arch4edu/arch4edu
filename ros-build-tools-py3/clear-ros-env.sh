#!/bin/bash

# See https://wiki.ros.org/ROS/EnvironmentVariables
# Required ROS environment variables
unset ROS_ROOT

# Additional PATH Environment Variables
unset ROS_PACKAGE_PATH

# Additional Bash Environment Variables
unset ROS_LOCATIONS
unset ROS_WORKSPACE

# Build System Environment Variables
unset ROS_BOOST_ROOT
unset ROS_BINDEPS_PATH
unset ROS_LANG_DISABLE
unset ROS_OS_OVERRIDE

# See https://wiki.ros.org/ros_environment
unset ROS_DISTRO
unset ROS_ETC_DIR
unset ROS_VERSION
unset ROS_PYTHON_VERSION

# Taken from old clear-ros-env.sh
unset ROS_PACKAGE
unset ROS_MASTER
