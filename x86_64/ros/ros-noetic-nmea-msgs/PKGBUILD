pkgdesc="ROS - The nmea_msgs package contains messages related to data in the NMEA format."
url='http://ros.org/wiki/nmea_msgs'

pkgname='ros-noetic-nmea-msgs'
pkgver='1.1.0'
arch=('any')
pkgrel=2
license=('BSD')

ros_makedepends=(ros-noetic-std-msgs
  ros-noetic-catkin
  ros-noetic-message-generation)
makedepends=('cmake' 'git' 'ros-build-tools'
  ${ros_makedepends[@]})

ros_depends=(ros-noetic-std-msgs
  ros-noetic-message-runtime)
depends=(${ros_depends[@]})

_dir=nmea_msgs-$pkgver
source=("${_dir}"::"https://github.com/ros-drivers/nmea_msgs/archive/refs/tags/$pkgver.tar.gz")
md5sums=('SKIP')

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python3 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

