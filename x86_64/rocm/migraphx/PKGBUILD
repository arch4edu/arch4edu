# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=migraphx
pkgver=5.3.0
pkgrel=1
pkgdesc="AMD's graph optimization engine"
arch=('x86_64')
url="https://rocmsoftwareplatform.github.io/AMDMIGraphX/doc/html/"
license=('MIT')
depends=('hip' 'miopen' 'protobuf' 'msgpack-cxx' 'blaze')
makedepends=('rocm-cmake' 'nlohmann-json' 'half' 'pybind11')
_git='https://github.com/ROCmSoftwarePlatform/AMDMIGraphX'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('d0b7283f42e03fb38b612868b8c94f46f27a6e0b019ae95fde5b9086582a1c69')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

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
