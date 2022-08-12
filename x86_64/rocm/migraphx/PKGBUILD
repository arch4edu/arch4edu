# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=migraphx
pkgver=5.2.1
pkgrel=1
pkgdesc="AMD's graph optimization engine"
arch=('x86_64')
url="https://rocmsoftwareplatform.github.io/AMDMIGraphX/doc/html/"
license=('MIT')
depends=('hip' 'miopen' 'protobuf' 'msgpack-cxx' 'blaze')
makedepends=('cmake' 'rocm-cmake' 'nlohmann-json' 'half' 'pybind11')
_git='https://github.com/ROCmSoftwarePlatform/AMDMIGraphX'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('300d990e1b92ad27c3eba3e94ef34538730ca9556398b8b9f7d61d28bf66c57d')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  cmake -Wno-dev -B build \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/AMDMIGraphX-rocm-$pkgver"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
