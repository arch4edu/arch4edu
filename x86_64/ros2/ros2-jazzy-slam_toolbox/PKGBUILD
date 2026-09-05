# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=slam_toolbox
pkgname=ros2-jazzy-slam_toolbox
pkgver=2.8.5
pkgrel=1
pkgdesc="Slam Toolbox for lifelong mapping and localization in potentially massive maps with ROS 2 Jazzy"
url="https://github.com/SteveMacenski/slam_toolbox"
arch=('x86_64')
license=('LGPL-2.1-only')
depends=(
    'ros2-jazzy'
    'ros2-jazzy-bond'
    'ros2-jazzy-bondcpp'
    'ceres-solver'
    'suitesparse'
    'boost-libs'
    'onetbb'
    'qt5-base'
    'eigen'
)
makedepends=('cmake' 'boost')
source=("$pkgname-$pkgver.tar.gz::https://github.com/SteveMacenski/slam_toolbox/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('657de32eb37b9e39da80882f356438df6aa8d8898a17acdb62f7a4d0fa8d3f70')

prepare() {
    # G2O is find_package(... REQUIRED) but never linked or included in 2.8.5,
    # and g2o is not packaged; drop the vestigial hard requirement.
    sed -i '/find_package(G2O REQUIRED)/d' "$_pkgname-$pkgver/CMakeLists.txt"
}

build() {
    source /opt/ros/jazzy/setup.bash

    # Compiled nodes embed __FILE__ build paths.
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    # karto_sdk relies on EIGEN3_INCLUDE_DIRS which is empty on Arch; add the path explicitly.
    export CXXFLAGS+=" -I/usr/include/eigen3"

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    install -Dm644 "$_pkgname-$pkgver/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
