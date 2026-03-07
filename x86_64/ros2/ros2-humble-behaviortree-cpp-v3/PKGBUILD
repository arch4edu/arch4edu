# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgname=BehaviorTree.CPP
pkgname=ros2-humble-behaviortree-cpp-v3
pkgver=3.8.7
pkgrel=1
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
sha256sums=('8f8d4d98708b05a79c60ce7c968c09e32a539eedf6615489a4e19b2fa1db633d')

prepare() {
    sed -i 's/CMAKE_CXX_STANDARD 14/CMAKE_CXX_STANDARD 17/g' BehaviorTree.CPP-$pkgver/CMakeLists.txt
}

build() {
    source /opt/ros/humble/setup.bash
    export CXXFLAGS="${CXXFLAGS} -include cstdint -Wno-error=maybe-uninitialized"

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -Wno-dev
    
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
