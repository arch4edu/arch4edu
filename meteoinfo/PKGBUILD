# Contributor: Heavysink <winstonwu91@gmail.com>

pkgname=meteoinfo
pkgver=1.8.7
pkgrel=1
pkgdesc="An open source software suite to view and analyze meteorological and spatial data interactively (MeteoInfoMap) or do scientific computation and visualization (MeteoInfoLab)"
arch=("any")
url="http://meteothink.org"
license=("LGPL")
depends=("sh" "java-environment")
makedepends=("unzip")
source=("http://meteothink.org/downloads/files/MeteoInfo_${pkgver}.zip")
sha256sums=("0bd87e1510661f04a28b0d67e31002e2ee9abecb24b99cb772d1aa10b6c730f3")
noextract=()

package() {
  mkdir -p $pkgdir/opt
  mkdir -p $pkgdir/usr/bin
  unzip $srcdir/MeteoInfo_${pkgver}.zip -d $pkgdir/opt
  cd $pkgdir/opt/MeteoInfo
  chmod +x milab.sh mimap.sh
  rm *.exe *_mac.sh *.log
  cd $srcdir
  ln -s /opt/MeteoInfo/milab.sh $pkgdir/usr/bin/milab
  ln -s /opt/MeteoInfo/mimap.sh $pkgdir/usr/bin/mimap
}
