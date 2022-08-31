# Script generated with import_catkin_packages.py
# For more information: https://github.com/bchretien/arch-ros-stacks
pkgdesc="ROS - Mobile robot simulator http://rtvhub.com/Stage."
url='https://wiki.ros.org/stage'

pkgname='ros-noetic-stage'
pkgver='4.3.0'
arch=('any')
pkgrel=4
license=('GPL')

ros_makedepends=()
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]}
  fltk
  libjpeg-turbo
  gtk2
  libtool
  mesa
  glu
  pkg-config)

ros_depends=(ros-noetic-catkin)
depends=(${ros_depends[@]}
  libjpeg-turbo
  mesa
  glu
  fltk
  gtk2)

_dir="Stage-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/rtv/Stage/archive/v${pkgver}.tar.gz")
sha256sums=('f32cb6887146441fd34671975fa81ea76438ce447bc68a0a6a1b62b5233ad2d6')

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
