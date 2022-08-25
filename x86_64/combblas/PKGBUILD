# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: Christian Pfeiffer <cpfeiffer at live de>
# Contributor: Michael Straube <straubem gmx de>
# Contributor: xantares <xantares09 at hotmail dot com>

pkgname=combblas
_PkgName=CombBLAS
pkgver=2.0.0
pkgrel=1
pkgdesc="A library offering a set of linear algebra primitives for graph analytics"
arch=('x86_64')
url="https://github.com/PASSIONLab/CombBLAS"
license=("BSD")
depends=('openmpi')
makedepends=('cmake')
source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('632a94201a042a2a9aa86803f50ee38b7bf0aa1cfef6ba0eb34ea4007f79a679')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"
  # Some tests are computationally heavy MPI stuff, so avoid them
  cmake ../$_PkgName-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=OFF
  make
}

package() {
  cd "$srcdir/build"
  make DESTDIR="$pkgdir" install

  # Remove OS X leftover files
  find "$pkgdir" -name "*.DS_Store" -delete
  find "$pkgdir" -name "._*" -delete

  install -Dm644 ../$_PkgName-$pkgver/LICENSE \
    -t "$pkgdir/usr/share/licenses/$pkgname"

  # Add extra headers
  install -Dm644 ../$_PkgName-$pkgver/Applications/*.h \
    -t "$pkgdir/usr/include/CombBLAS/Applications"
  install -Dm644 ../$_PkgName-$pkgver/Applications/BipartiteMatchings/*.h \
    -t "$pkgdir/usr/include/CombBLAS/Applications/BipartiteMatchings"
}
