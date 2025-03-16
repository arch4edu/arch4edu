# Maintainer: Pavel Ruzicka <rossetti at seznam dot cz>
# Contributor: Alexandre Petitjean <alpetitjean_gmail dot_com>

pkgname=geographiclib
pkgver=2.5
pkgrel=2
pkgdesc="Set of C++ classes for conversions between geographic, UTM, UPS, MGRS, geocentric, and local cartesian coordinates, for gravity, geoid height, and geomagnetic field calculations and for solving geodesic problems. Geotrans replacement."
arch=('i686' 'x86_64')
url="https://github.com/geographiclib/geographiclib"
license=('MIT')
depends=('bash')
makedepends=('gcc' 'make' 'cmake')
options=('staticlibs' '!debug')

source=("$pkgname-$pkgver.tar.gz::https://github.com/geographiclib/geographiclib/archive/v${pkgver}.tar.gz")
sha256sums=('347319e3dc5dd2d58116ff1ecb8c0ae11c9f095c655fe289992b3208bc7a32fc')

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
