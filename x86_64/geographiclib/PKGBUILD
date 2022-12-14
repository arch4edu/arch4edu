# Maintainer: Pavel Ruzicka <rossetti at seznam dot cz>
# Contributor: Alexandre Petitjean <alpetitjean_gmail dot_com>

pkgname=geographiclib
_pkgname=GeographicLib
pkgver=2.1.2
pkgrel=1
pkgdesc="Set of C++ classes for conversions between geographic, UTM, UPS, MGRS, geocentric, and local cartesian coordinates, for gravity, geoid height, and geomagnetic field calculations and for solving geodesic problems. Geotrans replacement."
arch=('i686' 'x86_64')
url="https://geographiclib.sourceforge.io/"
license=('MIT')
depends=('bash')
makedepends=('gcc' 'make' 'cmake')
options=('staticlibs')

source=(https://sourceforge.net/projects/geographiclib/files/distrib-C%2B%2B/${_pkgname}-${pkgver}.tar.gz/download)
md5sums=('8b0010429ebda99e624b51dfa06bbbed')

install=geographiclib.install

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  cmake ./ \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_BOTH_LIBS=ON
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # move scripts from /usr/sbin to /usr/bin - due to pacman >= 4.2 directory symlink handling
  mv ${pkgdir}/usr/sbin/* ${pkgdir}/usr/bin
  rm -r ${pkgdir}/usr/sbin
}
