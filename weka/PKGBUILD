# Maintainer: Jonathon Fernyhough <jonathon+m2x+dev>
# Contributor: Aitor Alonso <mail@aalonso.pw>
# Contributor: Andrew Chen <andrew.chuanye.chen@gmail.com>
# Contributor: mmm
# Contributor: Dan McGee <dan@archlinux.org>

pkgname=weka
pkgver=3.8.6
_dlver=${pkgver//./-}
pkgrel=2
pkgdesc="A collection of machine learning algorithms for data mining tasks"
url="https://www.cs.waikato.ac.nz/ml/weka/"
license=("GPL")
arch=('any')
source=(https://downloads.sourceforge.net/sourceforge/$pkgname/$pkgname-$_dlver.zip
        weka.sh
        weka.desktop
        weka.png)
sha256sums=('7e57405331f01c07ed84d9e0ffa07548cddf70877e4518fcd016c117e8c6e867'
            'd40e6131a7fd14f97b41f2db46053114ae986a8a0c4dc0001cb3f78b5d723dc1'
            'b68628d484e775c90a3d6554837ee3be7dc7ef356a7107184da7136effa247c1'
            '6cb96deb1e8634048032400674faf2ef869ac090deee66d637051a5d1af42655')

package() {
  depends=('java-runtime=11')

  # Desktop launcher, icon, wrapper script
  install -Dm644 weka.desktop "$pkgdir"/usr/share/applications/weka.desktop
  install -Dm644 weka.png     "$pkgdir"/usr/share/pixmaps/weka.png
  install -D     weka.sh      "$pkgdir"/usr/bin/weka

  cd $pkgname-$_dlver

  # jar file
  install -Dm644 weka.jar "$pkgdir"/usr/share/$pkgname/weka.jar

  # Documentation
  install -Dm644 -t "$pkgdir"/usr/share/doc/$pkgname documentation.* README *.pdf weka.gif
  cp -dr --no-preserve=ownership doc "$pkgdir"/usr/share/doc/$pkgname/
   
  # Example data files
  install -Dm644 -t "$pkgdir"/usr/share/$pkgname/data data/*
}
