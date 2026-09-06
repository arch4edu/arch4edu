# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=robot_localization
pkgname=ros2-jazzy-robot_localization
pkgver=3.8.3
pkgrel=1
pkgdesc="ROS 2 package of nonlinear state estimation nodes (EKF/UKF) for mobile robots"
url="https://index.ros.org/p/robot_localization/"
arch=('x86_64')
license=('BSD-3-Clause')
depends=(
    'ros2-jazzy'
    'ros2-jazzy-angles'
    'ros2-jazzy-geographic_msgs'
    'ros2-jazzy-diagnostic_updater'
    'boost-libs'
    'eigen'
    'geographiclib'
)
makedepends=(
    'cmake'
    'boost'
    'ros2-jazzy-angles'
    'ros2-jazzy-geographic_msgs'
    'ros2-jazzy-diagnostic_updater'
)
source=("$_pkgname-$pkgver.tar.gz::https://github.com/cra-ros-pkg/robot_localization/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('5df092e75dabb00f42c12c74f9f251f8f9c85286a54055ba88f1462f90b359c9')

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$srcdir/$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
