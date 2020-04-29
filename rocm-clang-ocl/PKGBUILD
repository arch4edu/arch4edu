# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Lucas Magalhães <whoisroot@national.shitposting.agency>
pkgname=rocm-clang-ocl
pkgver=3.3.0
pkgrel=1
pkgdesc="OpenCL compilation with clang compiler."
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/clang-ocl"
license=('unknown')
makedepends=('cmake' 'hcc' 'rocm-cmake')
source=("${pkgname}-${pkgver}::https://github.com/RadeonOpenCompute/clang-ocl/archive/rocm-$pkgver.tar.gz")
sha256sums=('d64dd00959bbc74781738eda6fc9b1379005d7160f9373134e471c4330c641b7')
_pkgname=clang-ocl

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DOPENCL_ROOT=/opt/rocm/hcc \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/$_pkgname-rocm-$pkgver"

  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
}
