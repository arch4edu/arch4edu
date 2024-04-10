# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
_base=testng
pkgname=java-${_base}
pkgver=7.10.1
pkgrel=1
arch=(any)
pkgdesc="A testing framework inspired by JUnit and NUnit"
url="https://${_base}.org"
license=(Apache-2.0)
depends=('java-runtime-openjdk=11')
makedepends=(gradle)
source=(${_base}-${pkgver}.tar.gz::https://github.com/${_base}-team/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('ff7296b6797659ba09edb510129a5725ec69ea38c9dcd9812e422c7d3a512c69b3d03b18b61546da2ad8a67acf17010ce0ce2629d6a8ae9fa3e217ea5d0e7c80')

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
