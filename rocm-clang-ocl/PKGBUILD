# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Lucas Magalhães <whoisroot@national.shitposting.agency>
pkgname=rocm-clang-ocl
pkgver=3.1.0
pkgrel=1
pkgdesc="OpenCL compilation with clang compiler."
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/clang-ocl"
license=('unknown')
makedepends=('cmake' 'hcc')
source=("${pkgname}-${pkgver}::http://github.com/RadeonOpenCompute/clang-ocl/archive/roc-${pkgver}.tar.gz")
sha256sums=('af93e626564cee2b3f6f5c2da0b5b95a9894f7357d895b259a706d38a57f1ef6')
_pkgname=clang-ocl

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DOPENCL_ROOT=/opt/rocm/hcc \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/$_pkgname-roc-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
}
