# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=navigation2
_pkgname=nav2_simple_commander
pkgname=ros2-humble-nav2-simple-commander
pkgver=1.1.7
pkgrel=3
pkgdesc="An importable library for writing mobile robot applications in python3"
url="https://index.ros.org/p/nav2_simple_commander/"
arch=('any')
makedepends=('python-pytest' 'cmake')
depends=(
    'ros2-humble' 
    'ros2-humble-nav2-msgs'
)
source=("https://github.com/ros-planning/navigation2/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('1d89dc1ad7c75d4d1645c882a5aee037ca965908344a158bb9669ad80a85196b')


build() {
    cd $_pkgroot-$pkgver/$_pkgname
    source /opt/ros/humble/setup.bash
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgroot-$pkgver/$_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
}
