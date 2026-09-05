# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-sdformat_urdf
pkgname=(
    'ros2-jazzy-sdformat_test_files'
    'ros2-jazzy-sdformat_urdf'
)
pkgver=1.0.2
pkgrel=1
pkgdesc="Convert SDFormat XML into a ROS 2 URDF C++ structure"
url="https://github.com/ros/sdformat_urdf"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=('cmake' 'urdfdom-headers' 'tinyxml2' 'ros2-jazzy-sdformat_vendor')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros/sdformat_urdf/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('a6cb7b23fcf4243cc87a7de35a42b0d8dd3376f0a25e0599d84a9b93ca58c5d4')

_srcname="sdformat_urdf-$pkgver"

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
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$_sub"
    DESTDIR="$srcdir/_staging/$_sub" cmake --install "$srcdir/build-$_sub"
}

build() {
    rm -rf "$srcdir/_staging"

    # sdformat_urdf embeds __FILE__ build paths in its plugin library.
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake sdformat_test_files
    _build_cmake sdformat_urdf
}

package_ros2-jazzy-sdformat_test_files() {
    pkgdesc="SDFormat sample model files used by sdformat_urdf tests"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/sdformat_test_files/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/sdformat_urdf/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-sdformat_urdf() {
    pkgdesc="Convert SDFormat XML into a ROS 2 URDF C++ structure"
    depends=('ros2-jazzy' 'ros2-jazzy-sdformat_vendor' 'sdformat14')

    cp -a "$srcdir/_staging/sdformat_urdf/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/sdformat_urdf/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
