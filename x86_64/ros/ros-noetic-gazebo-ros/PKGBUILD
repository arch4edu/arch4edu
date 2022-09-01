# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - Provides ROS plugins that offer message and service publishers
for interfacing with Gazebo through ROS."
url='http://wiki.ros.org/gazebo_ros'

pkgname='ros-noetic-gazebo-ros'
pkgver='2.9.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('Apache 2.0')

ros_makedepends=(
  ros-noetic-catkin
  ros-noetic-cmake-modules
  ros-noetic-gazebo-dev
)

makedepends=(
  cmake
  ros-build-tools
  ${ros_makedepends[@]}
)

ros_depends=(
  ros-noetic-gazebo-dev
  ros-noetic-gazebo-msgs
  ros-noetic-roslib
  ros-noetic-roscpp
  ros-noetic-tf
  ros-noetic-std-srvs
  ros-noetic-rosgraph-msgs
  ros-noetic-dynamic-reconfigure
  ros-noetic-std-msgs
  ros-noetic-geometry-msgs
)

depends=(
  ${ros_depends[@]}
  tinyxml
  python-argparse
)

_dir="gazebo_ros_pkgs-${pkgver}/gazebo_ros"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-simulation/gazebo_ros_pkgs/archive/${pkgver}.tar.gz")

sha256sums=('db937f15e5bf8f804de5d8dc0b67607f8b354aecde35785b6bff2d43387abff4')

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCMAKE_CXX_STANDARD=17
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
