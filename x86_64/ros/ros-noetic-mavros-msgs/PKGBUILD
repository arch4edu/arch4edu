# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - mavros_msgs defines messages for MAVROS."
url='https://wiki.ros.org/mavros_msgs'

pkgname='ros-noetic-mavros-msgs'
pkgver=1.17.0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('GPLv3, LGPLv3, BSD')

ros_makedepends=(
  ros-noetic-catkin
  ros-noetic-message-generation
)

makedepends=(
  cmake
  ros-build-tools
  ${ros_makedepends[@]}
)

ros_depends=(
  ros-noetic-message-runtime
  ros-noetic-std-msgs
  ros-noetic-geometry-msgs
  ros-noetic-sensor-msgs
  ros-noetic-geographic-msgs
)

depends=(
  ${ros_depends[@]}
)

_dir="mavros-release-upstream-${pkgver}/mavros_msgs"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mavlink/mavros-release/archive/refs/tags/upstream/${pkgver}.tar.gz")
sha256sums=('251fbb37b09e7d1bd662f03762e39db1552b33457f9bd8f2d6470c7678054091')

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

  # Build project
  cmake -Wno-dev -B build -S ${_dir} \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make -sC build
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
