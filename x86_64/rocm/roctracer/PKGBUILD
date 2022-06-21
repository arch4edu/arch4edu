# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=roctracer
pkgver=5.1.3
pkgrel=1
pkgdesc="ROCm Tracer Callback/Activity Library for Performance tracing AMD GPU's"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html#amd-rocm-roctracer'
license=('MIT')
depends=('hip' 'rocprofiler')
makedepends=('cmake' 'git' 'python-argparse' 'python-cppheaderparser' 'python-ply')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/roctracer'
source=("roctracer-rocm-$pkgver.tar.gz::$_git/archive/refs/tags/rocm-$pkgver.tar.gz"
        "glibc-2.34.patch::https://patch-diff.githubusercontent.com/raw/ROCm-Developer-Tools/roctracer/pull/63.patch")
sha256sums=('45f19875c15eb609b993788b47fd9c773b4216074749d7744f3a671be17ef33c'
            '937e040a045eceddb609f18df1106f17fbe69b0ca479dea43fb794d58cacf7c2')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/glibc-2.34.patch"
}

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
