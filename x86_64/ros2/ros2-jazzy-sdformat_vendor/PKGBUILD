# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgname=ros2-jazzy-sdformat_vendor
pkgver=0.0.14
pkgrel=1
pkgdesc="ROS 2 Jazzy vendor wrapper for system sdformat14"
arch=('x86_64')
url="https://github.com/gazebo-release/sdformat_vendor"
license=('Apache-2.0')
depends=('ros2-jazzy' 'sdformat14')
makedepends=('cmake' 'tinyxml2' 'urdfdom' 'pybind11')
source=("sdformat_vendor-$pkgver.tar.gz::https://github.com/gazebo-release/sdformat_vendor/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('08aa5b3873763cd749a85143210f4fd09c2ccda62fa0577246d6d45b67fb5309')

prepare() {
    # gz_tools_vendor is not packaged separately; the system gz-tools2 already
    # satisfies the requirement, so drop the vendor dependency.
    sed -i '/gz_tools_vendor/d' \
        "$srcdir/sdformat_vendor-$pkgver/package.xml" \
        "$srcdir/sdformat_vendor-$pkgver/CMakeLists.txt"
}

build() {
    source /opt/ros/jazzy/setup.bash
    cmake -B build -S "$srcdir/sdformat_vendor-$pkgver" \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/sdformat_vendor-$pkgver/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
