# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=control_toolbox
pkgname=ros2-jazzy-control_toolbox
pkgver=4.11.1
pkgrel=1
pkgdesc="Control modules useful across ROS 2 controllers, for Jazzy"
url="https://github.com/ros-controls/control_toolbox"
arch=('x86_64')
license=('Apache-2.0' 'BSD-3-Clause')
depends=(
    'ros2-jazzy'
    'ros2-jazzy-backward_ros'
    'ros2-jazzy-control_msgs'
    'ros2-jazzy-filters'
    'ros2-jazzy-generate_parameter_library'
    'ros2-jazzy-realtime_tools'
    'ros2-jazzy-rsl'
    'ros2-jazzy-tcb_span'
    'ros2-jazzy-tl_expected'
    'tl-expected'
    'eigen'
    'fmt'
)
makedepends=('cmake' 'ros2-jazzy-ros2_control_cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ros-controls/control_toolbox/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('a9cf0dc25f30cdab0b00e3c7e2579f3af4285bfa8c986a83c506fb1cebad228e')

_srcname="control_toolbox-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$_srcname/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE.Apache-2.0"
    install -Dm644 "$_srcname/LICENSE.BSD-3-clause" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE.BSD-3-Clause"
}
