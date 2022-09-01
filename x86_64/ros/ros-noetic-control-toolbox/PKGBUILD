# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - The control toolbox contains modules that are useful across all controllers."
url='https://wiki.ros.org/control_toolbox'

pkgname='ros-noetic-control-toolbox'
pkgver='1.19.0'
_pkgver_patch=0
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('BSD')

ros_makedepends=(ros-noetic-dynamic-reconfigure
  ros-noetic-std-msgs
  ros-noetic-roscpp
  ros-noetic-catkin
  ros-noetic-control-msgs
  ros-noetic-realtime-tools
  ros-noetic-message-generation
  ros-noetic-cmake-modules)
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]}
  tinyxml)

ros_depends=(ros-noetic-dynamic-reconfigure
  ros-noetic-std-msgs
  ros-noetic-message-runtime
  ros-noetic-roscpp
  ros-noetic-control-msgs
  ros-noetic-realtime-tools
  ros-noetic-cmake-modules)
depends=(${ros_depends[@]}
  tinyxml)

# Git version (e.g. for debugging)
# _tag=release/noetic/control_toolbox/${pkgver}-${_pkgver_patch}
# _dir=${pkgname}
# source=("${_dir}"::"git+https://github.com/ros-gbp/control_toolbox-release.git"#tag=${_tag})
# sha256sums=('SKIP')

# Tarball version (faster download)
_dir="control_toolbox-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-controls/control_toolbox/archive/${pkgver}.tar.gz")
sha256sums=('437ee9cd49b836646000674435140d222d45c5f916a83b4d2c935e21f3d1a1e7')

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
