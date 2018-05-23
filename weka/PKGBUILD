# Maintainer: Aitor Alonso <mail@aalonso.pw>
# Contributor: Andrew Chen <andrew.chuanye.chen@gmail.com>
# Contributor: mmm
# Contributor: Dan McGee <dan@archlinux.org>

pkgname=weka
pkgver=3.8.2
_dlver=${pkgver//./-}
pkgrel=1
pkgdesc="A collection of machine learning algorithms for data mining tasks"
url="http://www.cs.waikato.ac.nz/ml/weka/"
license=("GPL")
arch=('any')
depends=('java-runtime')
makedepends=('java-environment' 'gif2png')
source=(http://downloads.sourceforge.net/sourceforge/weka/$pkgname-$_dlver.zip
        weka.sh
        weka.desktop)
md5sums=('491f1efa03a6406f524f934d481059d6'
         'e3c18faba03e827a24b5d8029e1825e1'
         '83a4d47ba64df90a92a38b23a14c6480')

build() {
  cd $srcdir/$pkgname-$_dlver

  # rip icon out of jar for use in desktop menu
  jar xf weka.jar weka/gui/weka_icon.gif || return 1
  gif2png -O weka/gui/weka_icon.gif || return 1
}

package() {
  cd $srcdir/$pkgname-$_dlver

  # install jar file
  mkdir -p $pkgdir/usr/share/java/$pkgname
  install -m644 weka.jar $pkgdir/usr/share/java/$pkgname/weka.jar

  # setup for freedesktop icons and shell script
  mkdir -p $pkgdir/usr/share/{applications,pixmaps}
  mkdir -p $pkgdir/usr/bin
  install -m644 weka/gui/weka_icon.png $pkgdir/usr/share/pixmaps/weka.png
  install -m644 $srcdir/weka.desktop $pkgdir/usr/share/applications/weka.desktop
  install -m755 $srcdir/weka.sh $pkgdir/usr/bin/weka
}
