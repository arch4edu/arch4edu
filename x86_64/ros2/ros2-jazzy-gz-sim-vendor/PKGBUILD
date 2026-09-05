# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgname=ros2-jazzy-gz-sim-vendor
pkgver=0.0.13
pkgrel=1
pkgdesc="ROS 2 Jazzy vendor wrapper for system gz-sim8"
arch=('x86_64')
url="https://github.com/gazebo-release/gz_sim_vendor"
license=('Apache-2.0')
depends=(
    'ros2-jazzy'
    'ros2-jazzy-gz-msgs-vendor'
    'ros2-jazzy-gz-transport-vendor'
    'gz-sim8'
)
makedepends=('cmake')
source=("gz_sim_vendor-$pkgver.tar.gz::https://github.com/gazebo-release/gz_sim_vendor/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('73a3c159e2bbcd6d12c3b14214e58359605813bbfb1b5ace0e0925447040d329')

prepare() {
    local _vendor
    for _vendor in gz_common_vendor gz_fuel_tools_vendor gz_gui_vendor \
        gz_physics_vendor gz_plugin_vendor gz_rendering_vendor \
        gz_sensors_vendor gz_tools_vendor sdformat_vendor; do
        sed -i "/$_vendor/d" \
            "$srcdir/gz_sim_vendor-$pkgver/package.xml" \
            "$srcdir/gz_sim_vendor-$pkgver/CMakeLists.txt"
    done
}

build() {
    source /opt/ros/jazzy/setup.bash
    cmake -B build -S "$srcdir/gz_sim_vendor-$pkgver" \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/gz_sim_vendor-$pkgver/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
