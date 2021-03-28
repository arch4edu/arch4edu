# Maintainer: Camille Monière <draslorus at draslorus dot fr>
# Contributor: Evgeniy Alekseev <arcanis at archlinux dot org>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Alexander Rødseth <rodseth at gmail dot com>
# Contributor: William Rea <sillywilly at gmail dot com>

pkgname=libmatio
pkgver=1.5.21
pkgrel=1
pkgdesc='C library with a fortran 90/95 module interface for reading/writing MATLAB MAT-files'
arch=('x86_64')
license=('custom:BSD')
url='https://sourceforge.net/projects/matio'
depends=('zlib' 'hdf5')
options=('!emptydirs')
source=("https://github.com/tbeu/matio/releases/download/v${pkgver}/matio-${pkgver}.tar.gz")
changelog=ChangeLog
sha512sums=('b00bcad807e6a7e10afa656eb77a0e3e9fb08d9cecc3e94ba41ef91ce60367d6686e6d387a874bbb83eb2f895d4a97caac554a70e7f5f6f5cb750052702d411c')

build() {
  cd "matio-${pkgver}"
  ./configure --prefix=/usr --enable-shared --with-hdf5
  make
}

package() {
  cd "matio-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rm -r "${pkgdir}/usr/share/info/dir"
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

