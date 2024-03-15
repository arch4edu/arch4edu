# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
_base=testng
pkgname=java-${_base}
pkgver=7.9.0
pkgrel=1
arch=(any)
pkgdesc="A testing framework inspired by JUnit and NUnit"
url="https://${_base}.org"
license=(Apache-2.0)
depends=('java-runtime-openjdk=11')
makedepends=(gradle)
source=(${_base}-${pkgver}.tar.gz::https://github.com/${_base}-team/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('8871fc2950ba746dec9e4d615b038e2ac32cec7010751231c13bc4ac2fad9f1211830c6809b99e0d566a69b49a8ed4cab9a7e7b13a2292a49007cdaad5fcb6de')

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
