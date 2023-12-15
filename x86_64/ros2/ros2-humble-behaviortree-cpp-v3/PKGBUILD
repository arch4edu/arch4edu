# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgname=BehaviorTree.CPP
pkgname=ros2-humble-behaviortree-cpp-v3
pkgver=3.8.3
pkgrel=3
pkgdesc="Behavior Trees Library in C++. Batteries included."
url="https://index.ros.org/p/behaviortree_cpp/"
arch=('any')
depends=(
    'ros2-humble'
    'boost-libs'
    'zeromq'
    'ncurses'
)
makedepends=('cmake' 'boost')
source=("https://github.com/BehaviorTree/BehaviorTree.CPP/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('5dd782cc73913b0bfe26adb6fe3d7c10f1e2063a0a994bcba4d4e2ac86470196')

prepare() {
    sed -i 's/CMAKE_CXX_STANDARD 14/CMAKE_CXX_STANDARD 17/g' BehaviorTree.CPP-$pkgver/CMakeLists.txt
}

build() {
    source /opt/ros/humble/setup.bash

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -Wno-dev
    
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
