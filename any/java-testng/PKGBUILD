# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-${_pkgname}
pkgver=7.5
pkgrel=1
pkgdesc='A testing framework inspired by JUnit and NUnit'
arch=('any')
url="http://testng.org"
license=('Apache')
depends=('jdk8-openjdk')
makedepends=('gradle')
source=("$pkgname-$pkgver.tar.gz::https://github.com/cbeust/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('fe99f601949f39cbc79f921a6291d59b0fa4e2f55a22c24e084325296fe486a4')

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
