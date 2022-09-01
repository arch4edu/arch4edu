pkgdesc="ROS - Controller for a differential drive mobile base."
url='https://github.com/ros-controls/ros_controllers/wiki'

pkgname='ros-noetic-diff-drive-controller'
pkgver='0.20.0'
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(
    ros-noetic-catkin
    ros-noetic-pluginlib
    ros-noetic-urdf
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    boost
)

ros_depends=(
    ros-noetic-controller-interface
    ros-noetic-control-msgs
    ros-noetic-dynamic-reconfigure
    ros-noetic-geometry-msgs
    ros-noetic-hardware-interface
    ros-noetic-nav-msgs
    ros-noetic-realtime-tools
    ros-noetic-tf
    ros-noetic-pluginlib
    ros-noetic-urdf
    ros-noetic-controller-manager
    ros-noetic-controller-manager-msgs
)

depends=(
    ${ros_depends[@]}
)

_dir="ros_controllers-${pkgver}/diff_drive_controller"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-controls/ros_controllers/archive/${pkgver}.tar.gz")
sha256sums=('c9a42db66d8a90604f255592fb0f2c20d315a235a0a20aaa07a1e045dcda6d27')

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
