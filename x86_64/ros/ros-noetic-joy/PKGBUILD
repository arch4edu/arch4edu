pkgdesc="ROS - ROS driver for a generic Linux joystick."
url='https://wiki.ros.org/joy'

pkgname='ros-noetic-joy'
pkgver='1.15.0'
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
pkgrel=2
license=('BSD')

ros_makedepends=(
    ros-noetic-diagnostic-updater
    ros-noetic-roscpp
    ros-noetic-sensor-msgs
    ros-noetic-catkin
    ros-noetic-roslint
)
makedepends=(
    cmake
    ros-build-tools
    ${ros_makedepends[@]}
    linuxconsole
)

ros_depends=(
    ros-noetic-diagnostic-updater
    ros-noetic-roscpp
    ros-noetic-sensor-msgs
)
depends=(
    ${ros_depends[@]}
    linuxconsole
    python-empy
)

_dir="joystick_drivers-${pkgver}/joy"
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/ros-drivers/joystick_drivers/archive/${pkgver}.tar.gz")
sha256sums=('37e82742674a5fd4cf9959051aeae3bb961da74f254f891909d10589266166ad')

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
