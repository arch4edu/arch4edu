# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-$_pkgname
pkgver=7.8.0
pkgrel=1
arch=(any)
pkgdesc='A testing framework inspired by JUnit and NUnit'
url="http://testng.org"
license=(Apache)
depends=(jdk11-openjdk)
makedepends=(gradle)
source=($pkgname-$pkgver.tar.gz::https://github.com/cbeust/$_pkgname/archive/$pkgver.tar.gz)
sha256sums=('94337f64dfc2d461adf9d3a7c6db9d0e4174ae314a061108713b2e8e7f28fe0a')

prepare() {
  echo "It's recommended to build in a clean chroot"
  unset _JAVA_OPTIONS

  cd "$srcdir/$_pkgname-$pkgver"
  sed -i '/enableFeaturePreview("VERSION_CATALOGS")/d' settings.gradle.kts
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
