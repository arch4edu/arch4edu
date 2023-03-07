# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=migraphx
pkgver=5.4.3
pkgrel=1
pkgdesc="AMD's graph optimization engine."
arch=('x86_64')
url="https://rocmsoftwareplatform.github.io/AMDMIGraphX/doc/html/"
license=('MIT')
depends=('hip' 'miopen' 'protobuf' 'msgpack-cxx' 'blaze')
makedepends=('rocm-cmake' 'nlohmann-json' 'half' 'pybind11')
_git='https://github.com/ROCmSoftwarePlatform/AMDMIGraphX'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "include-array.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/AMDMIGraphX/pull/1435.patch"
        "msgpack.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/AMDMIGraphX/pull/1603.patch")
sha256sums=('f83e7bbe5d6d0951fb2cf0abf7e8b3530e9a5e45f7cec6d760da055d6905d568'
            'SKIP'
            'SKIP')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/include-array.patch"
    patch -Np1 -i "$srcdir/msgpack.patch"
}

build() {
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
