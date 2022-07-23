# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=roctracer
pkgver=5.2.1
pkgrel=1
pkgdesc="ROCm Tracer Callback/Activity Library for Performance tracing AMD GPU's"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html#amd-rocm-roctracer'
license=('MIT')
depends=('hip' 'rocprofiler')
makedepends=('cmake' 'git' 'python-argparse' 'python-cppheaderparser' 'python-ply')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/roctracer'
source=("roctracer-rocm-$pkgver.tar.gz::$_git/archive/refs/tags/rocm-$pkgver.tar.gz")
sha256sums=('e200b5342bdf840960ced6919d4bf42c8f30f8013513f25a2190ee8767667e59')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm

  cd "$srcdir"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
