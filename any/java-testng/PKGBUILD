# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
_base=testng
pkgname=java-${_base}
pkgver=7.10.0
pkgrel=1
arch=(any)
pkgdesc="A testing framework inspired by JUnit and NUnit"
url="https://${_base}.org"
license=(Apache-2.0)
depends=('java-runtime-openjdk=11')
makedepends=(gradle)
source=(${_base}-${pkgver}.tar.gz::https://github.com/${_base}-team/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('090e0a7f075505cdbecc456e65f00353f98d6b1122586cd229a9795a9b624aa76c6efeb0464c83fbdd8b4515f7ccaf7bc53e3e4f13260a963c11e561e2b97c2c')

prepare() {
  echo "It's recommended to build in a clean chroot"
  unset _JAVA_OPTIONS

  cd ${_base}-${pkgver}
  # https://github.com/testng-team/testng/issues/3054
  sed -i '/enableFeaturePreview("VERSION_CATALOGS")/d' settings.gradle.kts
}

build() {
  cd ${_base}-${pkgver}
  gradle --daemon clean build || true
}

package() {
  cd ${_base}-${pkgver}/$_base/build/libs
  install -Dm644 $_base-$pkgver-SNAPSHOT-all.jar \
    "$pkgdir/usr/share/java/$_base/$_base-$pkgver.jar"

  install -Dm 644 ${srcdir}/${_base}-${pkgver}/LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
