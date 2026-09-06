# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-cpp_polyfills
pkgname=(
    'ros2-jazzy-tcb_span'
    'ros2-jazzy-tl_expected'
)
pkgver=1.3.2
pkgrel=1
pkgdesc="C++ standard library polyfills for ROS 2 Jazzy"
url="https://github.com/PickNikRobotics/cpp_polyfills"
arch=('any')
makedepends=('cmake' 'ros2-jazzy')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/PickNikRobotics/cpp_polyfills/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('2914d24b9f0079436aaf8242ed030236adfa3e744e0d729df7adce3063cbf410')

_srcname="cpp_polyfills-$pkgver"

_build_sub() {
    local sub="$1"
    source /opt/ros/jazzy/setup.bash
    cmake -B "$srcdir/build-$sub" -S "$srcdir/$_srcname/$sub" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build "$srcdir/build-$sub"
    DESTDIR="$srcdir/stage-$sub" cmake --install "$srcdir/build-$sub"
}

build() {
    _build_sub tcb_span
    _build_sub tl_expected
}

package_ros2-jazzy-tcb_span() {
    pkgdesc="Implementation of C++20 std::span for ROS 2 Jazzy"
    license=('BSL-1.0')
    depends=('ros2-jazzy')
    cp -a "$srcdir/stage-tcb_span/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/tcb_span/LICENSE_1_0.txt" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-tl_expected() {
    pkgdesc="C++11/14/17 std::expected implementation for ROS 2 Jazzy"
    license=('CC0-1.0')
    depends=('ros2-jazzy')
    cp -a "$srcdir/stage-tl_expected/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/tl_expected/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
