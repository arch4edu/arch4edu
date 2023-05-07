# $Id: PKGBUILD 226630 2017-05-03 13:48:02Z spupykin $
# Maintainer: Geballin - Guillaume Ballin <macniaque at free dot fr>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=bwidget
pkgver=1.9.16
pkgrel=2
pkgdesc="A suite of megawidgets for Tk"
arch=('any')
url="https://wiki.tcl.tk/2251"
license=('GPL')
depends=('bash' 'tcl')
source=("http://downloads.sourceforge.net/project/tcllib/BWidget/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('bfe0036374b84293d23620a7f6dda86571813d0c7adfed983c1f337e5ce81ae0')

package() {
  cd "${srcdir}"
  install -d "${pkgdir}"/usr/lib/tcl8.6
  cp -r bwidget-$pkgver "${pkgdir}"/usr/lib/tcl8.6/
  chmod -R 755  "${pkgdir}"/usr/lib/tcl8.6/*
}
