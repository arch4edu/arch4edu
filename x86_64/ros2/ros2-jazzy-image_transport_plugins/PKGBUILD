# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-image_transport_plugins
pkgname=(
    'ros2-jazzy-compressed_image_transport'
    'ros2-jazzy-compressed_depth_image_transport'
    'ros2-jazzy-theora_image_transport'
    'ros2-jazzy-zstd_image_transport'
    'ros2-jazzy-image_transport_plugins'
)
pkgver=4.0.7
pkgrel=1
pkgdesc="ROS 2 image_transport plugins (compressed, compressed-depth, theora, zstd)"
url="https://index.ros.org/p/image_transport_plugins/"
arch=('x86_64')
license=('BSD-3-Clause' 'MIT')
depends=('ros2-jazzy')
makedepends=('cmake' 'ros2-jazzy-cv_bridge' 'opencv4' 'libogg' 'libtheora' 'pkgconf' 'zlib')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-perception/image_transport_plugins/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c28fdf269cb2cc146c35f3f40f2a1bf215eeec07b70287c1b5bbdd8565f0e583')

_srcname="image_transport_plugins-$pkgver"

_build_cmake() {
    local _sub="$1"
    shift

    source /opt/ros/jazzy/setup.bash

    local _prefix='' _dep
    for _dep in "$@"; do
        _prefix+="$srcdir/_staging/$_dep/opt/ros/jazzy:"
    done

    CMAKE_PREFIX_PATH="${_prefix}${CMAKE_PREFIX_PATH}" \
        cmake -B "$srcdir/build-$_sub" -S "$srcdir/$_srcname/$_sub" \
            -DCMAKE_BUILD_TYPE='None' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -DOpenCV_DIR='/usr/lib/cmake/opencv4' \
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$_sub"
    DESTDIR="$srcdir/_staging/$_sub" cmake --install "$srcdir/build-$_sub"
}

build() {
    rm -rf "$srcdir/_staging"

    # Match cv_bridge's OpenCV 4 headers; remap embedded build paths.
    export CFLAGS+=" -I/usr/include/opencv4 -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -I/usr/include/opencv4 -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake compressed_image_transport
    _build_cmake compressed_depth_image_transport
    _build_cmake theora_image_transport
    _build_cmake zstd_image_transport
    _build_cmake image_transport_plugins \
        compressed_image_transport compressed_depth_image_transport \
        theora_image_transport zstd_image_transport
}

package_ros2-jazzy-compressed_image_transport() {
    pkgdesc="image_transport plugin for JPEG/PNG compressed images"
    depends=('ros2-jazzy' 'ros2-jazzy-cv_bridge' 'opencv4')
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/compressed_image_transport/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-compressed_depth_image_transport() {
    pkgdesc="image_transport plugin for compressed depth images"
    depends=('ros2-jazzy' 'ros2-jazzy-cv_bridge' 'opencv4')
    license=('BSD-3-Clause' 'MIT')

    cp -a "$srcdir/_staging/compressed_depth_image_transport/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-theora_image_transport() {
    pkgdesc="image_transport plugin for Theora video streaming"
    depends=('ros2-jazzy' 'ros2-jazzy-cv_bridge' 'opencv4' 'libogg' 'libtheora')
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/theora_image_transport/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-zstd_image_transport() {
    pkgdesc="image_transport plugin using zlib compression"
    depends=('ros2-jazzy' 'zlib')
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/zstd_image_transport/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-image_transport_plugins() {
    pkgdesc="Metapackage pulling in all image_transport plugins"
    depends=(
        'ros2-jazzy-compressed_image_transport'
        'ros2-jazzy-compressed_depth_image_transport'
        'ros2-jazzy-theora_image_transport'
        'ros2-jazzy-zstd_image_transport'
    )
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/image_transport_plugins/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
