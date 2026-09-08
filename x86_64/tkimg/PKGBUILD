# Maintainer:  Andrew O'Neill <andrew at haunted dot sh>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Martin C. Doege <mdoege at compuserve dot com>
# Contributor: kotyz <kotyz.king@gmail.com>

pkgname=tkimg
_pkgname=Img
pkgver=2.1.2
pkgrel=1
pkgdesc='Provides the handling of several image formats beyond the standard formats in Tk'
url='https://wiki.tcl-lang.org/page/Img'
arch=('x86_64')
license=('TCL')
depends=('zlib' 'libjpeg-turbo' 'libpng' 'libtiff' 'tcl' 'tk' 'tcllib')
source=("https://downloads.sourceforge.net/${pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('932d386142e5aaff74add63da283d0547f0515d6155b9a2b69b433f9c353271a')

build() {
  cd "${_pkgname}-${pkgver}"

  ./configure --prefix=/usr --enable-64bit --enable-threads
  make all
}

package() {
  cd "${_pkgname}-${pkgver}"

  make INSTALL_ROOT="${pkgdir}" install
  install -Dm644 license.terms "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
