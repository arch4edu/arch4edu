# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=navigation2
_pkgname=nav2_costmap_2d
pkgname=ros2-humble-nav2-costmap-2d
pkgver=1.1.7
pkgrel=2
pkgdesc="This package provides an implementation of a 2D costmap that takes in sensor data from the world, builds a 2D or 3D occupancy grid of the data"
url="https://index.ros.org/p/nav2_costmap_2d/"
arch=('any')
makedepends=(
    'ros2-humble-nav2-common'
    'ros2-humble-nav2-map-server'
    'ros2-humble-nav2-lifecycle-manager'
    'cmake'
)
depends=(
    'ros2-humble' 
    'ros2-humble-nav2-msgs'
    'ros2-humble-nav2-util'
    'ros2-humble-nav2-voxel-grid'
    'ros2-humble-angles'
)
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
