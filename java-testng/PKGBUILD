# Maintainer: Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-${_pkgname}
pkgver=7.0.0
pkgrel=1
pkgdesc='A testing framework inspired by JUnit and NUnit'
arch=('any')
url="http://testng.org"
license=('Apache')
depends=("jdk8-openjdk" "java-runtime")
source=("https://github.com/cbeust/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('62a844cf3618beef667bb9901716e312e76d9244db7ec7ac655ba9505a026835')

build() {
  cd $srcdir/$_pkgname-$pkgver
  ./gradlew --daemon clean build
}

check() {
  cd $srcdir/$_pkgname-$pkgver
  ./gradlew --daemon test
}

package() {
  install -Dm644 \
    $srcdir/$_pkgname-$pkgver/build/libs/$_pkgname-$pkgver-SNAPSHOT.jar \
    $pkgdir/usr/share/java/$_pkgname/$_pkgname-$pkgver.jar
}
