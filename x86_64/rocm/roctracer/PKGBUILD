# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=roctracer
pkgver=5.3.0
pkgrel=1
pkgdesc='ROCm tracer library for performance tracing'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html#amd-rocm-roctracer'
license=('MIT')
depends=('hip' 'rocprofiler')
makedepends=('cmake' 'git' 'python-argparse' 'python-cppheaderparser' 'python-ply')
_git='https://github.com/ROCm-Developer-Tools/roctracer'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/refs/tags/rocm-$pkgver.tar.gz")
sha256sums=('36f1da60863a113bb9fe2957949c661f00a702e249bb0523cda1fb755c053808')
options=('!lto')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  cmake \
    -B build \
    -Wno-dev \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DHIP_ROOT_DIR=/opt/rocm/hip
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
