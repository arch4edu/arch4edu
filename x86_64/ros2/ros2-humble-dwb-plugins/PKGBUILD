# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=navigation2
_pkgname=nav2_dwb_controller/dwb_plugins
pkgname=ros2-humble-dwb-plugins
pkgver=1.1.7
pkgrel=2
pkgdesc="Standard implementations of the GoalChecker and TrajectoryGenerators for dwb_core"
url="https://index.ros.org/p/dwb_plugins/"
arch=('any')
depends=(
    'ros2-humble'
    'ros2-humble-angles'
    'ros2-humble-dwb-core'
    'ros2-humble-nav2-util'
    'ros2-humble-nav-2d-msgs'
    'ros2-humble-nav-2d-utils'
)
makedepends=('cmake')
source=("https://github.com/ros-planning/navigation2/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('1d89dc1ad7c75d4d1645c882a5aee037ca965908344a158bb9669ad80a85196b')


build() {
    source /opt/ros/humble/setup.bash

    cmake -B build -S "$_pkgroot-$pkgver/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -Wno-dev
    
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
