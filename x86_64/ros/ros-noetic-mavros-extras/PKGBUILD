pkgdesc="ROS - Extra nodes and plugins for MAVROS."
url='https://wiki.ros.org/mavros_extras'

pkgname='ros-noetic-mavros-extras'
pkgver=1.15.0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('GPLv3, LGPLv3, BSD')

ros_makedepends=(ros-noetic-std-msgs
  ros-noetic-tf
  ros-noetic-mavros
  ros-noetic-mavros-msgs
  ros-noetic-roscpp
  ros-noetic-catkin
  ros-noetic-urdf
  ros-noetic-geometry-msgs
  ros-noetic-visualization-msgs
  ros-noetic-sensor-msgs
  ros-noetic-cmake-modules)
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]})

ros_depends=(ros-noetic-tf
  ros-noetic-std-msgs
  ros-noetic-mavros-msgs
  ros-noetic-roscpp
  ros-noetic-urdf
  ros-noetic-geometry-msgs
  ros-noetic-mavros
  ros-noetic-visualization-msgs
  ros-noetic-sensor-msgs)
depends=(${ros_depends[@]}
	 geographiclib)

_dir="mavros-release-upstream-${pkgver}/mavros_extras"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mavlink/mavros-release/archive/refs/tags/upstream/${pkgver}.tar.gz")
sha256sums=('0d9207a1548d051c0e9fe6630197c48599d720c9833b5be618b9d7857ef01ca8')

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

  # Build project
  cmake -Wno-dev -B build -S ${_dir} \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python \
        -DCMAKE_CXX_STANDARD=17 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make -sC build
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
