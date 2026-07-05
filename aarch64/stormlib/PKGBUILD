# Maintainer: Jerome Leclanche <jerome@leclan.ch>
# Co-maintainer: robertfoster

_pkgname=StormLib
pkgname=stormlib
pkgver=9.40 # renovate: datasource=github-tags depName=ladislav-zezula/StormLib
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

sha256sums=('f80b08bae168888702a4251312d6c2279f487673df611c2b5ef4f395e810c3b1')
