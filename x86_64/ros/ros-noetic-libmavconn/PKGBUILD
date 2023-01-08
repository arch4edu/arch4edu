pkgdesc="ROS - MAVLink communication library."
url='https://wiki.ros.org/libmavconn'

pkgname='ros-noetic-libmavconn'
pkgver=1.15.0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('GPLv3, LGPLv3, BSD')

ros_makedepends=(
  ros-noetic-mavlink
  ros-noetic-catkin
)
makedepends=(
  cmake
  ros-build-tools
  ${ros_makedepends[@]}
  boost
  console-bridge
)

ros_depends=(ros-noetic-mavlink)
depends=(
  ${ros_depends[@]}
  boost
  console-bridge
)

_dir="mavros-${pkgver}/libmavconn"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mavlink/mavros/archive/${pkgver}.tar.gz")
sha256sums=('784776cc212fcc4f5fe4e346b063ca30f3a921d8e370e0a92dfb53356cf2e6fe')

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
