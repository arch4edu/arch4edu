# Maintainer: robertfoster
pkgname=smpq
pkgver=1.7
pkgrel=1
pkgdesc="StormLib MPQ archiving utility. Designed for full manipulating with Blizzard MPQ archives"
arch=('i686' 'x86_64')
url="https://launchpad.net/smpq"
license=('GPL3')
depends=('bzip2' 'stormlib' 'zlib')
makedepends=('cmake')
source=("https://launchpad.net/smpq/trunk/${pkgver}/+download/smpq_${pkgver}.orig.tar.gz")

build() {
  cd "${srcdir}"

  cmake \
    -B "${srcdir}/build" \
    -S "${srcdir}/${pkgname}-${pkgver}" \
    -DWITH_KDE=OFF \
    -DCMAKE_INSTALL_PREFIX=/usr

  cmake --build build
}

package() {
  cd "${srcdir}"
  DESTDIR="${pkgdir}" cmake --install "${srcdir}/build"
}

sha256sums=('b9f99f13b31adaa792e320a02a405a322cb7669ad484781bf2fffeffbf749de2')
