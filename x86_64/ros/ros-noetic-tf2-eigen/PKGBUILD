pkgdesc="ROS - tf2_eigen."
url='https://wiki.ros.org/tf2_eigen'

pkgname='ros-noetic-tf2-eigen'
pkgver='0.7.5'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
    ros-noetic-tf2
    ros-noetic-catkin
    ros-noetic-geometry-msgs
    ros-noetic-cmake-modules
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    eigen
)

ros_depends=(
    ros-noetic-tf2
    ros-noetic-geometry-msgs
)

depends=(
    ${ros_depends[@]}
    eigen
)

_dir="geometry2-${pkgver}/tf2_eigen"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/geometry2/archive/${pkgver}.tar.gz")
sha256sums=('0b5d461c71d6dc1dbdb99a2ba39e1515194cd451c2e53d53caadb3ecea13367a')

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
