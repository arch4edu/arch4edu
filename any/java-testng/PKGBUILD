# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
_base=testng
pkgname=java-${_base}
pkgver=7.10.2
pkgrel=1
arch=(any)
pkgdesc="A testing framework inspired by JUnit and NUnit"
url="https://${_base}.org"
license=(Apache-2.0)
depends=('java-runtime-openjdk=11')
makedepends=(gradle)
source=(${_base}-${pkgver}.tar.gz::https://github.com/${_base}-team/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('15b32ca8706c54599692aa59b83e8ed4deadf1e407cfc015506f6af182b22a664ac196b07bc34fe40d57f1b24149aa18cc84bfb7f7ffbf3437e158676b646657')

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
