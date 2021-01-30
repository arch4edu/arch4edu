# Maintainer: Camille Monière <draslorus at draslorus dot fr>
# Contributor: Evgeniy Alekseev <arcanis at archlinux dot org>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Alexander Rødseth <rodseth at gmail dot com>
# Contributor: William Rea <sillywilly at gmail dot com>

pkgname=libmatio
pkgver=1.5.19
pkgrel=1
pkgdesc='C library with a fortran 90/95 module interface for reading/writing MATLAB MAT-files'
arch=('x86_64')
license=('custom:BSD')
url='https://sourceforge.net/projects/matio'
depends=('zlib' 'hdf5')
options=('!emptydirs')
source=("https://downloads.sourceforge.net/matio/matio-${pkgver}.tar.gz")
changelog=ChangeLog
sha512sums=('c087944a7d87d78a7de662d7e19f5f81c55858cf5bf315c28d5a0f7544555b0816045e20bb0c83752eb3d54b589d9237a27cf3de98e3ebefcc7ea0af9311740e')

build() {
  cd "matio-${pkgver}"
  ./configure --prefix=/usr --enable-shared --with-hdf5 \
	--enable-mat73='yes' --with-default-file-ver='7.3' \
	--with-matlab=/dev/null
  make
}

package() {
  cd "matio-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rm -r "${pkgdir}/usr/share/info/dir"
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

