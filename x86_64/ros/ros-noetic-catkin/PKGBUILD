pkgdesc="ROS - Low-level build system macros and infrastructure for ROS."
url='https://wiki.ros.org/catkin'

pkgname='ros-noetic-catkin'
pkgver='0.8.10'
arch=('any')
pkgrel=2
license=('BSD')

ros_makedepends=(
)

makedepends=(
    cmake
    ${ros_makedepends[@]}
    python-catkin_pkg
    python-empy
    python
)

ros_depends=(
)

depends=(
    ${ros_depends[@]}
    python-nose
    gtest
    python-catkin_pkg
    python-empy
    gmock
    python
    ros-build-tools
)

_dir="catkin-${pkgver}/"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/catkin/archive/${pkgver}.tar.gz")
sha256sums=('363857f037d8f300a5889d00dc8248673f363d587d639c11e23f1f0fd3c22b92')

build() {
    # Use ROS environment variables.
    source /usr/share/ros-build-tools/clear-ros-env.sh
    [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

    # Create the build directory.
    [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
    cd ${srcdir}/build

    # Build the project.
    cmake ${srcdir}/${_dir} \
        -DCATKIN_BUILD_BINARY_PACKAGE=OFF \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
    make
}

package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}/" install
}
