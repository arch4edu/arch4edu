# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Contributor: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgname=BehaviorTree.CPP
pkgname=ros2-jazzy-behaviortree-cpp-v3
pkgver=3.8.8
pkgrel=1
pkgdesc="Behavior Trees Library in C++. Batteries included."
url="https://index.ros.org/p/behaviortree_cpp/"
arch=('x86_64')
license=('MIT')
depends=(
    'ros2-jazzy'
    'boost-libs'
    'zeromq'
    'ncurses'
)
makedepends=('cmake' 'boost')
source=("$pkgname-$pkgver.tar.gz::https://github.com/BehaviorTree/BehaviorTree.CPP/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('7b87e4819f0c482639c30fa6a6f06ab4c83c10e3362032cfc3beff4d827205af')

build() {
    source /opt/ros/jazzy/setup.bash

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -Wno-dev

    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
