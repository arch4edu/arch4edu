# $Id: PKGBUILD 226630 2017-05-03 13:48:02Z spupykin $
# Maintainer: Geballin - Guillaume Ballin <macniaque at free dot fr>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=bwidget
pkgver=1.9.15
pkgrel=1
pkgdesc="A suite of megawidgets for Tk"
arch=('any')
url="https://wiki.tcl.tk/2251"
license=('GPL')
depends=('bash' 'tcl')
source=("http://downloads.sourceforge.net/project/tcllib/BWidget/$pkgver/$pkgname-$pkgver.tar.bz2")
sha256sums=('9c4dd648fdfd31de7cb5af44b392a1916f949dd195820684d940edcd8485ac13')

package() {
  cd "${srcdir}"
  install -d "${pkgdir}"/usr/lib/tcl8.6
  cp -r bwidget-$pkgver "${pkgdir}"/usr/lib/tcl8.6/
}
