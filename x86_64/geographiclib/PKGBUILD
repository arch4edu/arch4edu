# Maintainer: Pavel Ruzicka <rossetti at seznam dot cz>
# Contributor: Alexandre Petitjean <alpetitjean_gmail dot_com>

pkgname=geographiclib
pkgver=2.5.2
pkgrel=1
pkgdesc="Set of C++ classes for conversions between geographic, UTM, UPS, MGRS, geocentric, and local cartesian coordinates, for gravity, geoid height, and geomagnetic field calculations and for solving geodesic problems. Geotrans replacement."
arch=('i686' 'x86_64')
url="https://github.com/geographiclib/geographiclib"
license=('MIT')
depends=('bash')
makedepends=('gcc' 'make' 'cmake')
options=('staticlibs' '!debug')

source=("$pkgname-$pkgver.tar.gz::https://github.com/geographiclib/geographiclib/archive/v${pkgver}.tar.gz")
sha256sums=('15485087b91722d1115229e983e0bce96869f5cea6049278381132d24865e919')

install=geographiclib.install

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cmake ./ \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_BOTH_LIBS=ON
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # move scripts from /usr/sbin to /usr/bin - due to pacman >= 4.2 directory symlink handling
  mv ${pkgdir}/usr/sbin/* ${pkgdir}/usr/bin
  rm -r ${pkgdir}/usr/sbin
}
