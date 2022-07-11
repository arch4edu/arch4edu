# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-${_pkgname}
pkgver=7.6.1
pkgrel=1
pkgdesc='A testing framework inspired by JUnit and NUnit'
arch=('any')
url="http://testng.org"
license=('Apache')
depends=('jdk11-openjdk')
makedepends=('gradle')
source=("$pkgname-$pkgver.tar.gz::https://github.com/cbeust/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('78ccf9122b62a2d4bdff90cab219254997f4120a94da49f72f2df2f2ea65c870')

prepare() {
  echo "It's recommended to build in a clean chroot"
  unset _JAVA_OPTIONS
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  gradle --daemon clean build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver/$_pkgname/build/libs"
  install -Dm644 $_pkgname-$pkgver-SNAPSHOT-all.jar \
    "$pkgdir/usr/share/java/$_pkgname/$_pkgname-$pkgver.jar"
}
