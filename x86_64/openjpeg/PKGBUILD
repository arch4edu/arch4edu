# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=openjpeg
pkgver=1.5.2
pkgrel=3
pkgdesc="An open source JPEG 2000 codec"
arch=('x86_64')
license=('BSD')
url="https://www.openjpeg.org"
depends=('zlib')
makedepends=('libtiff' 'lcms2' 'libpng' 'doxygen')
optdepends=('lcms2: j2k_to_image and image_to_j2k programs'
            'libpng: j2k_to_image and image_to_j2k programs')
source=(http://downloads.sourceforge.net/openjpeg.mirror/${pkgname}-${pkgver}.tar.gz)
sha512sums=('b945cf4f8b5e3227a0c07120c94b0ed5bf30c901de73059ee1d47975f46744fb62bbe84cdb2917c6431128f400020874eb07160af870b5448ced897998b08862')

build() {
  cd $pkgname-$pkgver
  autoreconf -fi
  # make sure we use system libs
  rm -rf thirdparty
  ./configure --prefix=/usr \
	--enable-shared --disable-static --disable-silent-rules
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="${pkgdir}" install
  install -m755 -d "${pkgdir}/usr/share/licenses/openjpeg"
  install -m644 LICENSE "${pkgdir}/usr/share/licenses/openjpeg/LICENSE"
}
