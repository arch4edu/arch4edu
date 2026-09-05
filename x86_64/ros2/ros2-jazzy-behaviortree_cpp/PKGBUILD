# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=behaviortree_cpp
pkgname=ros2-jazzy-behaviortree_cpp
pkgver=4.10.0
pkgrel=1
pkgdesc="Behavior Trees library for task planning and execution (v4, for ROS 2 Jazzy)"
url="https://index.ros.org/p/behaviortree_cpp/"
arch=('x86_64')
license=('MIT')
depends=('ros2-jazzy' 'sqlite' 'zeromq' 'tinyxml2')
makedepends=('cmake' 'cppzmq')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/BehaviorTree/BehaviorTree.CPP/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c758fdedb3666f7ca4c9998a4c0b243251e0a5fb5d03c99e2ee63d615af7a71d')

_srcname="BehaviorTree.CPP-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$srcdir/$_srcname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -DBTCPP_EXAMPLES=OFF \
        -DBTCPP_UNIT_TESTS=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/$_srcname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
