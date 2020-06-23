pkgname=zfp
pkgver=0.5.5
pkgrel=1
pkgdesc="Library for compressed numerical array"
arch=('x86_64')
url="https://computation.llnl.gov/projects/floating-point-compression"
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake')
source=("https://github.com/LLNL/zfp/releases/download/$pkgver/zfp-$pkgver.tar.gz")
sha256sums=('fdf7b948bab1f4e5dccfe2c2048fd98c24e417ad8fb8a51ed3463d04147393c5')

build() {
  cd "$srcdir/zfp-$pkgver"
  mkdir -p build && pushd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib ..
  make
}

check() {
  cd "$srcdir/zfp-$pkgver/build"
  ctest --output-on-failure
}

package() {
  cd "$srcdir/zfp-$pkgver/build"
  make DESTDIR="$pkgdir" install
}

