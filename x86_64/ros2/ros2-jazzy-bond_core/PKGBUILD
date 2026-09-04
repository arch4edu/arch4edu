# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Contributor: Jingbei Li <i@jingbei.li>

pkgbase=ros2-jazzy-bond_core
pkgname=(
    'ros2-jazzy-bond'
    'ros2-jazzy-smclib'
    'ros2-jazzy-bondcpp'
    'ros2-jazzy-bondpy'
    'ros2-jazzy-bond_core'
)
pkgver=4.2.0
pkgrel=1
pkgdesc="A bond allows two processes, A and B, to know when the other has terminated"
url="https://index.ros.org/p/bond/"
arch=('x86_64')
license=('BSD-3-Clause' 'MPL-1.1')
depends=('ros2-jazzy')
makedepends=('cmake' 'python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros/bond_core/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('40eb58edb084fea0f1ecf191254c5062a406d667dfc9863b3c3491d7d4f115d5')

_srcname="bond_core-$pkgver"

# Configure, build and stage one ament_cmake subpackage. Remaining arguments
# name already-staged subpackages this one needs on CMAKE_PREFIX_PATH.
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
            -DCMAKE_BUILD_TYPE='Release' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -Wno-dev
    cmake --build "$srcdir/build-$_sub"
    DESTDIR="$srcdir/_staging/$_sub" cmake --install "$srcdir/build-$_sub"
}

build() {
    rm -rf "$srcdir/_staging"

    # rcutils logging embeds __FILE__ in libbondcpp.so.
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    # Dependency order: bond and smclib are leaves, the other two consume them.
    _build_cmake bond
    _build_cmake smclib
    _build_cmake bondcpp bond smclib
    _build_cmake bond_core bond smclib

    cd "$srcdir/$_srcname/bondpy"
    source /opt/ros/jazzy/setup.bash
    python -m build --wheel --no-isolation
}

package_ros2-jazzy-bond() {
    pkgdesc="Message and service definitions for bond"
    depends=('ros2-jazzy')
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/bond/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/bond/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-smclib() {
    pkgdesc="The State Machine Compiler runtime library"
    depends=('ros2-jazzy')
    license=('MPL-1.1')

    cp -a "$srcdir/_staging/smclib/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/smclib/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-bondcpp() {
    pkgdesc="C++ implementation of bond"
    depends=('ros2-jazzy' 'ros2-jazzy-bond' 'ros2-jazzy-smclib')
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/bondcpp/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/bondcpp/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-bondpy() {
    pkgdesc="Python implementation of bond"
    depends=('ros2-jazzy' 'ros2-jazzy-bond' 'ros2-jazzy-smclib' 'python')
    license=('BSD-3-Clause')

    python -m installer --destdir="$pkgdir" --prefix='/opt/ros/jazzy' \
        "$srcdir/$_srcname/bondpy/dist/"*.whl
    install -Dm644 "$srcdir/$_srcname/bondpy/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-bond_core() {
    pkgdesc="Metapackage pulling in the full bond_core stack"
    depends=('ros2-jazzy-bond' 'ros2-jazzy-bondcpp' 'ros2-jazzy-bondpy' 'ros2-jazzy-smclib')
    license=('BSD-3-Clause')

    cp -a "$srcdir/_staging/bond_core/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/bond_core/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
