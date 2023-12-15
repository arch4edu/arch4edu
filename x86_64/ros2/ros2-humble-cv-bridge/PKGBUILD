# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=vision_opencv
_pkgname=cv_bridge
pkgname=ros2-humble-cv-bridge
pkgver=3.2.1
pkgrel=4
pkgdesc="This contains CvBridge, which converts between ROS Image messages and OpenCV images."
url="https://index.ros.org/p/cv_bridge/"
arch=('any')
makedepends=(
    'boost'
    'cmake'
)
depends=(
    'ros2-humble'
    'opencv'
    'python-numpy'
    'python-opencv'
)
source=("https://github.com/ros-perception/vision_opencv/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('bf8a18770ffe3335e9bf96cb89be886a846be10382e67c2dc93cd4e387b2c3f9')


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
