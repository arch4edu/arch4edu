# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - The urdf_sim_tutorial package."
url='https://wiki.ros.org/urdf_sim_tutorial'

pkgname='ros-noetic-urdf-sim-tutorial'
pkgver='0.5.1'
_pkgver_patch=0
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(ros-noetic-catkin)
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]})

ros_depends=(ros-noetic-position-controllers
  ros-noetic-controller-manager
  ros-noetic-joint-state-controller
  ros-noetic-diff-drive-controller
  ros-noetic-urdf-tutorial
  ros-noetic-gazebo-ros-control
  ros-noetic-rqt-robot-steering
  ros-noetic-gazebo-ros
  ros-noetic-xacro
  ros-noetic-rviz
  ros-noetic-robot-state-publisher)
depends=(${ros_depends[@]})

# Git version (e.g. for debugging)
# _tag=release/noetic/urdf_sim_tutorial/${pkgver}-${_pkgver_patch}
# _dir=${pkgname}
# source=("${_dir}"::"git+https://github.com/ros-gbp/urdf_sim_tutorial-release.git"#tag=${_tag})
# sha256sums=('SKIP')

# Tarball version (faster download)
_dir="urdf_sim_tutorial-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/urdf_sim_tutorial/archive/${pkgver}.tar.gz")
sha256sums=('6f350a379fdfc2e30a11cabfa4cdf809afdd05e792e657546940e04122c42797')

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
