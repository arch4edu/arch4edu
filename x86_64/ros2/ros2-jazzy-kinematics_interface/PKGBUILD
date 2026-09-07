# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-kinematics_interface
pkgname=(
    'ros2-jazzy-kinematics_interface'
    'ros2-jazzy-kinematics_interface_kdl'
    'ros2-jazzy-kinematics_interface_pinocchio'
)
pkgver=1.7.1
pkgrel=1
pkgdesc="Kinematics interface and plugins for ROS 2 Jazzy"
url="https://github.com/ros-controls/kinematics_interface"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=('cmake' 'boost' 'ros2-jazzy-backward_ros' 'ros2-jazzy-ros2_control_cmake' 'pinocchio' 'eigen')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-controls/kinematics_interface/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('b36e9fc9ae55fb5a92e0eb5dcafd62de9be159dc251c9289bda3af8700c9b4ef')

_srcname="kinematics_interface-$pkgver"

_build_cmake() {
    local sub="$1"
    shift
    source /opt/ros/jazzy/setup.bash

    local prefix='' dep
    for dep in "$@"; do
        prefix+="$srcdir/stage-$dep/opt/ros/jazzy:"
    done

    CMAKE_PREFIX_PATH="${prefix}${CMAKE_PREFIX_PATH}" \
        cmake -B "$srcdir/build-$sub" -S "$srcdir/$_srcname/$sub" \
            -DCMAKE_BUILD_TYPE='None' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$sub"
    DESTDIR="$srcdir/stage-$sub" cmake --install "$srcdir/build-$sub"
}

build() {
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake kinematics_interface
    _build_cmake kinematics_interface_kdl kinematics_interface
    _build_cmake kinematics_interface_pinocchio kinematics_interface
}

_install_sub() {
    local sub="$1"
    cp -a "$srcdir/stage-$sub/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-kinematics_interface() {
    depends=('ros2-jazzy' 'ros2-jazzy-backward_ros' 'eigen')
    _install_sub kinematics_interface
}

package_ros2-jazzy-kinematics_interface_kdl() {
    depends=('ros2-jazzy' 'ros2-jazzy-backward_ros' 'ros2-jazzy-kinematics_interface' 'eigen')
    _install_sub kinematics_interface_kdl
}

package_ros2-jazzy-kinematics_interface_pinocchio() {
    depends=('ros2-jazzy' 'ros2-jazzy-kinematics_interface' 'pinocchio' 'eigen')
    _install_sub kinematics_interface_pinocchio
}
