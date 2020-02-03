# Maintainer: Jonathon Fernyhough <jonathon "at manjaro+dot+org>
# Contributor: Aitor Alonso <mail@aalonso.pw>
# Contributor: Andrew Chen <andrew.chuanye.chen@gmail.com>
# Contributor: mmm
# Contributor: Dan McGee <dan@archlinux.org>

pkgname=weka
pkgver=3.8.4
_dlver=${pkgver//./-}
pkgrel=2
pkgdesc="A collection of machine learning algorithms for data mining tasks"
url="http://www.cs.waikato.ac.nz/ml/weka/"
license=("GPL")
arch=('any')
depends=('java-runtime')
makedepends=('java-environment')
source=(https://downloads.sourceforge.net/sourceforge/$pkgname/$pkgname-$_dlver.zip
        weka.sh
        weka.desktop
        weka.png)
sha256sums=('ffca58c609d15b78775253f83850c23a0b8dcd57360b97058ceb94da0e0c6821'
            'e1c9d5cb72580b4305957a459e8475e120132e6fee872e4a8c8b9b6dbaf7709a'
            'b68628d484e775c90a3d6554837ee3be7dc7ef356a7107184da7136effa247c1'
            '6cb96deb1e8634048032400674faf2ef869ac090deee66d637051a5d1af42655')

package() {
  # Desktop launcher, icon, wrapper script
  install -Dm644 weka.desktop "$pkgdir"/usr/share/applications/weka.desktop
  install -Dm644 weka.png     "$pkgdir"/usr/share/pixmaps/weka.png
  install -Dm755 weka.sh      "$pkgdir"/usr/bin/weka

  # jar file
  cd $pkgname-$_dlver
  install -Dm644 weka.jar "$pkgdir"/usr/share/$pkgname/weka.jar

  # Documentation
  install -Dm644 -t "$pkgdir"/usr/share/doc/$pkgname documentation.* README *.pdf weka.gif
  cp -dr --no-preserve=ownership doc "$pkgdir"/usr/share/doc/$pkgname/
   
  # Example data files
  install -Dm644 -t "$pkgdir"/usr/share/$pkgname/data data/*
}
