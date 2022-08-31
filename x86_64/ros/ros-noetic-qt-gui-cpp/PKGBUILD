pkgdesc="ROS - qt_gui_cpp provides the foundation for C++-bindings for qt_gui and creates bindings for every generator available."
url='https://wiki.ros.org/qt_gui_cpp'

pkgname='ros-noetic-qt-gui-cpp'
pkgver='0.4.2'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('BSD')

ros_makedepends=(
    ros-noetic-catkin
    ros-noetic-cmake-modules
    ros-noetic-pluginlib
    ros-noetic-python-qt-binding
)

makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    python-setuptools
    pkg-config
    qt5-base
    tinyxml
)

ros_depends=(
    ros-noetic-pluginlib
    ros-noetic-qt-gui
)

depends=(
    ${ros_depends[@]}
    tinyxml
    sip
    python-sip
    sip4
    python-sip4
)

_dir="qt_gui_core-${pkgver}/qt_gui_cpp"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-visualization/qt_gui_core/archive/${pkgver}.tar.gz")
sha256sums=('fbc5a7b0a4da43f80e9216845aec2e247fac0a63512053c03a9f89024d026aad')

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
