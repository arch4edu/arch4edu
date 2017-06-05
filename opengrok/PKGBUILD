# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: kalenz <https://aur.archlinux.org/account/kalenz>
# Contributor: Vojtech Horky <vojta . horky at-symbol seznam . cz>
pkgname=opengrok
_pkgname=OpenGrok
pkgver=1.0
pkgrel=1
pkgdesc="A fast and usable source code search and cross reference engine, written in Java"
url="http://opengrok.github.io/OpenGrok/"
arch=('any')
license=('CDDL')
depends=('tomcat8' 'sh' 'java-runtime>=8' 'ctags' 'unzip')
source=("https://github.com/${pkgname}/${_pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha1sums=('79f3927b84a0667a481dece9d05f9ba20be5c520')

prepare() {
  cd ${pkgname}-${pkgver}
  # jre7 unsupported and doesn't work, hardcode jre8 java
  sed -i '2iJAVA=/usr/lib/jvm/java-8-openjdk/bin/java' bin/OpenGrok
}

package() {
  cd ${pkgname}-${pkgver}

  install -dm755 "$pkgdir/usr/share/java/opengrok"
  cp -r lib/ "$pkgdir/usr/share/java/opengrok"
  cp -r bin/ "$pkgdir/usr/share/java/opengrok"

  mkdir "$pkgdir/usr/bin"
  ln -s /usr/share/java/opengrok/bin/OpenGrok "$pkgdir/usr/bin/opengrok"
  install -dm755 "$pkgdir/usr/share/doc/opengrok"
  cp -r doc/* "$pkgdir/usr/share/doc/opengrok"
}
