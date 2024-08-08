# Maintainer: Maik93 <michael.mugnai@gmail.com>

# Script written starting from `ros-melodic-serial`

pkgdesc="ROS - Serial is a cross-platform, simple to use library for using serial ports on computers."
url="https://github.com/wjwwood/serial"

pkgname='ros-noetic-serial'
pkgver='1.2.1'
arch=('any')
pkgrel=1
license=('MIT')

ros_makedepends=(ros-noetic-catkin)
makedepends=('cmake' 'ros-build-tools' ${ros_makedepends[@]})

ros_depends=()
depends=(${ros_depends[@]})

# Tarball version (faster download)
_dir="serial-release-release-melodic-serial"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/wjwwood/serial-release/archive/release/melodic/serial/${pkgver}.tar.gz")
sha256sums=('3591de6b9035a647e0c3050109fb7d342681742e617bbf0e8f3d828e21b84c0f')

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
            -DCATKIN_ENABLE_TESTING=0 \
            -DCATKIN_BUILD_BINARY_PACKAGE=ON \
            -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
            -DSETUPTOOLS_DEB_LAYOUT=OFF
    make
}

package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}/" install
}
