# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: David Hajek <dante4d at gmail dot com>
# Contributor: Geoffroy Carrier <geoffroy dot carrier at koon dot fr>
# Contributor: Otto Allmendinger <otto.allmendinger@gmail.com>

pkgname=jgoodies-looks
pkgver=2.8.0
pkgrel=4
pkgdesc="A Java Swing look and feel library"
arch=('any')
url="http://www.jgoodies.com/"
license=('BSD')
groups=('jgoodies')
depends=('java-runtime')
#source=("http://www.jgoodies.com/download/libraries/looks/jgoodies-looks-${pkgver//./_}-20150402.zip")
source=("https://mrwitek.github.io/aur-repo/jgoodies-looks-2_8_0-20150402.zip")
md5sums=('89a28c43d742142869077e3ebeb109c9')
sha1sums=('6fd9cddd9ad82044dd603acb3a38a925cfa9e3e8')
sha256sums=('2b9382063f3058992db088fcf99fec04d41396b37e1e155f3af3b6c091435297')
sha512sums=('40b524f3ea082f322bda221cd57c58a97128625a51af6bbb86433d69e74bec4f366e551e9fafa0062bf98a1ee1786267906e6ec1994507f6b3b8d5d1148e42f7')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm644 "LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/license.txt"
  install -Dm644 "${pkgname}-${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
