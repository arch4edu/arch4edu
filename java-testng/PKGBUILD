# Maintainer: Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-${_pkgname}
pkgver=7.3.0
pkgrel=3
pkgdesc='A testing framework inspired by JUnit and NUnit'
arch=('any')
url="http://testng.org"
license=('Apache')
depends=('jdk8-openjdk')
makedepends=('gradle')
source=("$pkgname-$pkgver.tar.gz::https://github.com/cbeust/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('337e78528755af7e39acc1b84cc6f7eaa0e24d843359491ae7fc57df8d331444')

build() {
  unset _JAVA_OPTIONS
  cd "$srcdir/$_pkgname-$pkgver"
  gradle --daemon clean build
}

package() {
  install -Dm644 \
    "$srcdir/$_pkgname-$pkgver/build/libs/$_pkgname-$pkgver.jar" \
    "$pkgdir/usr/share/java/$_pkgname/$_pkgname-$pkgver.jar"
}
