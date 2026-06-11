# Maintainer:  Andrew O'Neill <andrew at haunted dot sh>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Martin C. Doege <mdoege at compuserve dot com>
# Contributor: kotyz <kotyz.king@gmail.com>

pkgname=tkimg
_pkgname=Img
pkgver=2.1.1
pkgrel=1
pkgdesc='Provides the handling of several image formats beyond the standard formats in Tk'
url='https://wiki.tcl-lang.org/page/Img'
arch=('x86_64')
license=('TCL')
depends=('zlib' 'libjpeg' 'libpng' 'libtiff' 'tcl' 'tk' 'tcllib')
source=("https://downloads.sourceforge.net/${pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('0e41efa886c470ca0c38663e66640eb6d89e9e5f746724535ac224e2509ae34f')

build() {
  cd "${_pkgname}-${pkgver}"

  CFLAGS+=" -ffat-lto-objects" ./configure --prefix=/usr --enable-64bit --enable-threads
  make all
}

package() {
  cd "${_pkgname}-${pkgver}"

  make INSTALL_ROOT="${pkgdir}" install
  install -Dm644 license.terms "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
