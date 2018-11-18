# Maintainer: Aitor Alonso <mail@aalonso.pw>
# Contributor: Andrew Chen <andrew.chuanye.chen@gmail.com>
# Contributor: mmm
# Contributor: Dan McGee <dan@archlinux.org>

pkgname=weka
pkgver=3.8.3
_dlver=${pkgver//./-}
pkgrel=1
pkgdesc="A collection of machine learning algorithms for data mining tasks"
url="http://www.cs.waikato.ac.nz/ml/weka/"
license=("GPL")
arch=('any')
depends=('java-runtime')
makedepends=('java-environment')
source=(http://downloads.sourceforge.net/sourceforge/weka/$pkgname-$_dlver.zip
        weka.sh
        weka.desktop
        weka.png)
md5sums=('1d2f24f40bc67ed2b7e530d54f8c7e6f'
         'e3c18faba03e827a24b5d8029e1825e1'
         '83a4d47ba64df90a92a38b23a14c6480'
         'f0fd36c73bc70e4f04cbdcd98b5fa862')

package() {
  cd $srcdir/$pkgname-$_dlver

  # install jar file
  mkdir -p $pkgdir/usr/share/java/$pkgname
  install -m644 weka.jar $pkgdir/usr/share/java/$pkgname/weka.jar

  # setup for freedesktop icons and shell script
  mkdir -p $pkgdir/usr/share/{applications,pixmaps}
  mkdir -p $pkgdir/usr/bin
  install -m644 $srcdir/weka.png $pkgdir/usr/share/pixmaps/weka.png
  install -m644 $srcdir/weka.desktop $pkgdir/usr/share/applications/weka.desktop
  install -m755 $srcdir/weka.sh $pkgdir/usr/bin/weka
}
