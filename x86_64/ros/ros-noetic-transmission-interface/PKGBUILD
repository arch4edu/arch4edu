# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - Transmission Interface."
url='https://github.com/ros-controls/ros_control/wiki'

pkgname='ros-noetic-transmission-interface'
pkgver='0.19.5'
_pkgver_patch=0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(ros-noetic-pluginlib
  ros-noetic-catkin
  ros-noetic-roscpp
  ros-noetic-hardware-interface
  ros-noetic-cmake-modules
  ros-noetic-resource-retriever)
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]}
  tinyxml)

ros_depends=(ros-noetic-pluginlib
  ros-noetic-roscpp)
depends=(${ros_depends[@]}
  tinyxml)

# Git version (e.g. for debugging)
# _tag=release/noetic/transmission_interface/${pkgver}-${_pkgver_patch}
# _dir=${pkgname}
# source=("${_dir}"::"git+https://github.com/ros-gbp/ros_control-release.git"#tag=${_tag})
# sha256sums=('SKIP')

# Tarball version (faster download)
_dir="ros_control-${pkgver}/transmission_interface"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-controls/ros_control/archive/${pkgver}.tar.gz")
sha256sums=('a9e031f7a4a448657f689971d8049351ec31776d15efac45c8c9b44b950f55b1')

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
