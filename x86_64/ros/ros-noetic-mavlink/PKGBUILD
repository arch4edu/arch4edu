pkgdesc="ROS - MAVLink message marshaling library."
url='https://wiki.ros.org/mavlink'

pkgname='ros-noetic-mavlink'
pkgver='2022.8.8'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=1
license=('LGPLv3')

ros_makedepends=()
makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    python-lxml
    python-future
    python-distribute
    python
)

ros_depends=(
    ros-noetic-catkin
)
depends=(
    ${ros_depends[@]}
    python
)

_dir="mavlink-gbp-release-upstream-${pkgver}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mavlink/mavlink-gbp-release/archive/upstream/${pkgver}.tar.gz")
sha256sums=('7e154b376255d32c416a5398d124af63c10b9861ce16bdb8f5b70a3464d4831b')

build() {
    # Use ROS environment variables
    source /usr/share/ros-build-tools/clear-ros-env.sh
    [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

    # Build project
    export ROS_PYTHON_VERSION=3
    cmake -Wno-dev -B build -S ${_dir} \
          -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic
    make -sC build
}

package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}/" install
}
