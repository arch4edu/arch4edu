# Maintainer: Jerome Leclanche <jerome@leclan.ch>
# Co-maintainer: robertfoster

_pkgname=StormLib
pkgname=stormlib
pkgver=9.30
pkgrel=1
pkgdesc="A C/C++ API to read and write MPQ files with support for merged archives, patch MPQs and more."
arch=("i686" "x86_64")
url="http://www.zezula.net/en/mpq/stormlib.html"
license=("MIT")
depends=("bzip2" "libtomcrypt" "libtommath" "zlib")
makedepends=("cmake")
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ladislav-zezula/${_pkgname}/archive/v${pkgver}.tar.gz")

build() {
  mkdir -p build
  cd build
  cmake "${srcdir}/${_pkgname}-${pkgver}" \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_LIBTOMCRYPT=ON \
    -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}

sha256sums=('a709a6b034d206404f5297d85e474371203ff5483639955195d99b737bbf7dfe')
