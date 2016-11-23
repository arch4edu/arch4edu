# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: kalenz <https://aur.archlinux.org/account/kalenz>
# Contributor: Vojtech Horky <vojta . horky at-symbol seznam . cz>
pkgname=opengrok
_pkgname=OpenGrok
pkgver=0.12.1.6
pkgrel=1
pkgdesc="A fast and usable source code search and cross reference engine, written in Java"
url="http://opengrok.github.io/OpenGrok/"
arch=('any')
license=('CDDL')
depends=('tomcat8' 'sh' 'java-environment' 'ctags' 'unzip')
source=("https://github.com/${_pkgname}/${_pkgname}/files/467358/${pkgname}-${pkgver}.tar.gz.zip"
        'archlinux.patch'
        'deploy.sh')
sha1sums=('4bec1b2ae58131fb407b9ca8f18ac330b8624180'
          'cd646208b1b5e0837cf0efc7825b3ec6ed653324'
          '118514d7474006c9b98151403d3d7952b8a9cea6')

prepare() {
  # github sources are tarballs in zip files for some reason, extract the actual tarball
  bsdtar xf ${pkgname}-${pkgver}.tar.gz
  cd ${pkgname}-${pkgver}
  # remove JAVA_HOME instances and fix paths
  patch -p1 -i "$srcdir/archlinux.patch"
}

package() {
  cd ${pkgname}-${pkgver}

  install -dm755 "$pkgdir/usr/share/java/opengrok"
  cp -r lib/* "$pkgdir/usr/share/java/opengrok"

  install -Dm755 "bin/OpenGrok" "$pkgdir/usr/bin/opengrok"
  install -dm755 "$pkgdir/usr/share/doc/opengrok"
  cp -r doc/* "$pkgdir/usr/share/doc/opengrok"
}
