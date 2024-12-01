# Maintainer: envolution
# Contributor: Heavysink <winstonwu91@gmail.com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=meteoinfo
pkgver=3.9.7
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
sha256sums=('9f66f4f417d3e91fc0ff39f451d633286629111b9161913518efe0e6e7f9cbdc'
            '97628afebc60f026f5c2b25d7491c46a5c4ee61f693e7cfa07fbd2c03605979b'
            'cf8266555871205d3e119395fdd67d01ac03816a2568f39bc34f393c2ed3a0ed')

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
