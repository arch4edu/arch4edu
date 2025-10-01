# Maintainer: envolution
# Contributor: Heavysink <winstonwu91@gmail.com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=meteoinfo
pkgver=4.1.3
pkgrel=1
pkgdesc="MeteoInfo: GIS, scientific computation and visualization environment"
arch=("any")
url="http://meteothink.org"
license=("LGPL-3.0")
depends=("java-environment")
source=("http://meteothink.org/downloads/files/MeteoInfo_${pkgver}.zip"
  https://raw.githubusercontent.com/meteoinfo/MeteoInfo/refs/heads/master/LICENSE
  https://raw.githubusercontent.com/meteoinfo/MeteoInfo/refs/heads/master/README.md
)
sha256sums=('bbb4bb426abdd53d8a31513add890d26d95a8a27fd6288224db5fc77086b2cf5'
            '97628afebc60f026f5c2b25d7491c46a5c4ee61f693e7cfa07fbd2c03605979b'
            '3cf668325fdd689a49cf5aab59f2b53948d7df05248e121be6111e11969a128c')

package() {
  install -dm755 $pkgdir/opt
  install -dm755 $pkgdir/usr/bin
  cp -r MeteoInfo $pkgdir/opt
  chmod +x $pkgdir/opt/MeteoInfo/milab.sh $pkgdir/opt/MeteoInfo/mimap.sh
  ln -s /opt/MeteoInfo/milab.sh $pkgdir/usr/bin/milab
  ln -s /opt/MeteoInfo/mimap.sh $pkgdir/usr/bin/mimap
  install -Dm644 README.md $pkgdir/usr/share/doc/$pkgname/README.md
  install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
# vim:set ts=2 sw=2 et:
