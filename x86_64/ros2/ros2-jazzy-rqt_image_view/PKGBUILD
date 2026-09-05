# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=rqt_image_view
pkgname=ros2-jazzy-rqt_image_view
pkgver=1.3.0
pkgrel=1
pkgdesc="ROS 2 rqt plugin for displaying images using image_transport"
url="https://index.ros.org/p/rqt_image_view/"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy' 'ros2-jazzy-cv_bridge' 'ros2-jazzy-qt_gui_cpp' 'ros2-jazzy-rqt_gui_cpp' 'opencv4' 'qt5-base')
makedepends=('cmake' 'qt5-base' 'opencv4')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/ros-visualization/rqt_image_view/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('45fcb0376808cca1d8caa29bdd8b81a96e8c926d5e3cb2f1e9ec8830e15b56c5')

build() {
    source /opt/ros/jazzy/setup.bash

    # rqt_image_view links cv_bridge, which was built against the OpenCV 4
    # compat package; keep the include path consistent.
    export CFLAGS+=" -I/usr/include/opencv4"
    export CXXFLAGS+=" -I/usr/include/opencv4"

    cmake -B build -S "$srcdir/$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DOpenCV_DIR='/usr/lib/cmake/opencv4' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    # Upstream ships no LICENSE file; the BSD-3-Clause notice lives in the
    # source header block.
    sed -n '/Redistribution and use/,/POSSIBILITY OF SUCH DAMAGE/p' \
        "$srcdir/$_pkgname-$pkgver/src/rqt_image_view/image_view.cpp" \
        | sed 's|^ \* \{0,1\}||' > LICENSE
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
