# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - This package provides ROS specific hooks for stage."
url='https://wiki.ros.org/stage_ros'

pkgname='ros-noetic-stage-ros'
pkgver='1.8.0'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=4
license=('BSD')

ros_makedepends=(ros-noetic-tf
  ros-noetic-std-msgs
  ros-noetic-rostest
  ros-noetic-stage
  ros-noetic-catkin
  ros-noetic-std-srvs
  ros-noetic-roscpp
  ros-noetic-nav-msgs
  ros-noetic-sensor-msgs
  ros-noetic-geometry-msgs)
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]}
  glu
  boost)

ros_depends=(ros-noetic-tf
  ros-noetic-std-msgs
  ros-noetic-roscpp
  ros-noetic-stage
  ros-noetic-std-srvs
  ros-noetic-geometry-msgs
  ros-noetic-nav-msgs
  ros-noetic-sensor-msgs)
depends=(${ros_depends[@]}
  glu
  boost)

_dir="stage_ros-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-simulation/stage_ros/archive/${pkgver}.tar.gz")
sha256sums=('21fbe64e3a5f639ce88a69b3ae15eea38a9e2dbeedfb7f9bed21f787706973fb')

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
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
