# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgname=ros2-jazzy-gz-msgs-vendor
pkgver=0.0.8
pkgrel=1
pkgdesc="ROS 2 Jazzy vendor wrapper for system gz-msgs10"
arch=('x86_64')
url="https://github.com/gazebo-release/gz_msgs_vendor"
license=('Apache-2.0')
depends=('ros2-jazzy' 'gz-msgs10')
makedepends=('cmake')
source=("gz_msgs_vendor-$pkgver.tar.gz::https://github.com/gazebo-release/gz_msgs_vendor/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('ab8dc9c044a9e610857006632b19c3447bbfc6639515db85c754458bcb5db584')

prepare() {
    sed -i '/gz_tools_vendor/d' \
        "$srcdir/gz_msgs_vendor-$pkgver/package.xml" \
        "$srcdir/gz_msgs_vendor-$pkgver/CMakeLists.txt"
}

build() {
    source /opt/ros/jazzy/setup.bash
    cmake -B build -S "$srcdir/gz_msgs_vendor-$pkgver" \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/gz_msgs_vendor-$pkgver/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
