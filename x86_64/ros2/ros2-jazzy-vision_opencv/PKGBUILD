# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-vision_opencv
pkgname=(
    'ros2-jazzy-cv_bridge'
    'ros2-jazzy-image_geometry'
    'ros2-jazzy-vision_opencv'
)
pkgver=4.1.0
pkgrel=1
pkgdesc="ROS 2 interface between ROS and OpenCV (cv_bridge, image_geometry)"
url="https://index.ros.org/p/vision_opencv/"
arch=('x86_64')
license=('Apache-2.0' 'BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=('cmake' 'opencv4' 'boost' 'python-numpy')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-perception/vision_opencv/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('9b62869915c450d9477d0a4e5b8d1ba4686772d51fb0b379835c3fd465c37ec1')

_srcname="vision_opencv-$pkgver"

prepare() {
    # numpy 2.0 removed ndarray.newbyteorder(); use the dtype-based form.
    sed -i 's/im\.byteswap()\.newbyteorder()/im.byteswap().view(im.dtype.newbyteorder())/' \
        "$srcdir/$_srcname/cv_bridge/python/cv_bridge/core.py"
}

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

    # Build against the OpenCV 4 compat package; C++ sources embed __FILE__
    # build paths, so remap them to avoid a $srcdir reference.
    export CFLAGS+=" -I/usr/include/opencv4 -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -I/usr/include/opencv4 -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake cv_bridge
    _build_cmake image_geometry
    _build_cmake vision_opencv cv_bridge image_geometry
}

package_ros2-jazzy-cv_bridge() {
    pkgdesc="ROS 2 interface between ROS and OpenCV"
    depends=('ros2-jazzy' 'opencv4' 'boost-libs' 'python-numpy' 'python-opencv')

    cp -a "$srcdir/_staging/cv_bridge/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE-BSD" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE-BSD"
    install -Dm644 "$srcdir/$_srcname/LICENSE-Apache" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE-Apache"
}

package_ros2-jazzy-image_geometry() {
    pkgdesc="ROS 2 collection of methods for dealing with image and pixel geometry"
    depends=('ros2-jazzy' 'opencv4' 'python-opencv' 'python-deprecated')

    cp -a "$srcdir/_staging/image_geometry/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE-BSD" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE-BSD"
    install -Dm644 "$srcdir/$_srcname/LICENSE-Apache" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE-Apache"
}

package_ros2-jazzy-vision_opencv() {
    pkgdesc="Metapackage pulling in cv_bridge and image_geometry"
    depends=('ros2-jazzy-cv_bridge' 'ros2-jazzy-image_geometry')

    cp -a "$srcdir/_staging/vision_opencv/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE-BSD" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE-BSD"
    install -Dm644 "$srcdir/$_srcname/LICENSE-Apache" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE-Apache"
}
