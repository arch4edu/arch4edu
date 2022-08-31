# Script generated with import_catkin_packages.py.
# For more information: https://github.com/bchretien/arch-ros-stacks.
pkgdesc="ROS - rosclean: cleanup filesystem resources (e.g."
url='https://wiki.ros.org/rosclean'

pkgname='ros-noetic-rosclean'
pkgver='1.15.8'
arch=('any')
pkgrel=1
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
    python-rospkg
)

_dir="ros-${pkgver}/tools/rosclean"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros/ros/archive/${pkgver}.tar.gz")
sha256sums=('2cece46697585e55db415c5ddb4be935641b70c8a220f761a8e551225f133e40')

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
