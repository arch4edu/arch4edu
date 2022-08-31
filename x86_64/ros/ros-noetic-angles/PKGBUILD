# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - This package provides a set of simple math utilities to work with angles."
url='https://wiki.ros.org/angles'

pkgname='ros-noetic-angles'
pkgver='1.9.13'
arch=('any')
pkgrel=3
license=('BSD')

ros_makedepends=(
    ros-noetic-catkin
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    python-setuptools
)

ros_depends=(
)

depends=(
    ${ros_depends[@]}
)

_dir="angles-${pkgver}/angles"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/angles/archive/${pkgver}.tar.gz")
sha256sums=('0e2982e9e4759614702f18f5c25cb7a0a88d382f4a4fab845ca1587305db2fd6')

build() {
    # Use ROS environment variables.
    source /usr/share/ros-build-tools/clear-ros-env.sh
    [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

    # Create the build directory.
    [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
    cd ${srcdir}/build

    # Build the project.
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
