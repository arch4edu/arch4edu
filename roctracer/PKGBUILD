# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=roctracer
pkgver=4.0.0
pkgrel=1
pkgdesc="ROCm Tracer Callback/Activity Library for Performance tracing AMD GPU's"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html#amd-rocm-roctracer'
license=('MIT')
depends=('hip-rocclr')
makedepends=('cmake' 'git' 'python' 'python-argparse' 'python-cppheaderparser' 'python-ply')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/roctracer'
source=("roctracer-rocm-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'deprecated_string_split.patch')
sha256sums=('f47859a46173228b597c463eda850b870e810534af5efd5f2a746067ef04edee'
            '466d34242462c0b2016a82cc6bd90780b578e7a62d6f255b5ba8047fb6925bea')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
  cd "$_dirname"
  patch -Np1 -i "$srcdir/deprecated_string_split.patch"
}

build() {
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DHIP_VDI=1

  cd "$srcdir"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
