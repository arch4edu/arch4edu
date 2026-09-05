# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgname=ros2-jazzy-gz-transport-vendor
pkgver=0.0.9
pkgrel=1
pkgdesc="ROS 2 Jazzy vendor wrapper for system gz-transport13"
arch=('x86_64')
url="https://github.com/gazebo-release/gz_transport_vendor"
license=('Apache-2.0')
depends=('ros2-jazzy' 'ros2-jazzy-gz-msgs-vendor' 'gz-transport13')
makedepends=('cmake')
source=("gz_transport_vendor-$pkgver.tar.gz::https://github.com/gazebo-release/gz_transport_vendor/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('9812ffd4c3bb2fa8955a827bec6925f259d78ac6a108d5365870b84c1645c1b2')

prepare() {
    sed -i '/gz_tools_vendor/d' \
        "$srcdir/gz_transport_vendor-$pkgver/package.xml" \
        "$srcdir/gz_transport_vendor-$pkgver/CMakeLists.txt"
}

build() {
    source /opt/ros/jazzy/setup.bash
    cmake -B build -S "$srcdir/gz_transport_vendor-$pkgver" \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/gz_transport_vendor-$pkgver/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
