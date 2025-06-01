# Maintainer: Kino <cybao292261@163.com>

pkgname=gtest-src
pkgver=1.16.0
pkgrel=2
pkgdesc='Google Test Source - C++ testing utility'
url='https://github.com/google/googletest'
arch=('x86_64')
license=('BSD-3-Clause')
depends=("gtest")
_srcname=googletest-${pkgver}
source=("${_srcname}.tar.gz::https://github.com/google/googletest/archive/v${pkgver}.tar.gz"
  "https://github.com/google/googletest/pull/4539.patch")
sha512sums=('bec8dad2a5abbea8e9e5f0ceedd8c9dbdb8939e9f74785476b0948f21f5db5901018157e78387e106c6717326558d6642fc0e39379c62af57bf1205a9df8a18b'
            'b1130b7846f94db88ca57fd924c79d68579794e215e8dfeeb137a50639f58e53be1f9db003b05e8c703232175c46c23fb318d04623779322a741d2e197fbdd2a')
b2sums=('e5f301987fd4b73cfc8e900ac476b38444994c63bd2f334fdc58704f9e6e966cc03a2dba7ddc033624e89853a15b2592530a1180c3e56be7a28928ed370a9e27'
        '84724d5894a5641208b311232fcc349fa10d2f0b3e183993fa8fb6c53eec45723b0bac453f9dc0a4dd55a7f76507eaca5fba882be7c0c984f4044398d4f4cc5a')

prepare() {
  cd ${srcdir}/${_srcname}
  sed -i "s|GOOGLETEST_VERSION 1.14.0|GOOGLETEST_VERSION ${pkgver}|g" $srcdir/4539.patch
  patch -Np1 -i "${srcdir}/4539.patch" || true
}

package() {
  find "${pkgdir}" -name '*.pump' -printf 'Removing %P\n' -delete

  cd ${_srcname}
  install -Dm 644 cmake/googletest-version.cmake -t "${pkgdir}/usr/src/cmake"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm 644 README.md CONTRIBUTORS -t "${pkgdir}/usr/share/doc/${pkgname}"

  cd googletest
  install -Dm 644 cmake/* -t "${pkgdir}/usr/src/googletest/cmake"
  install -Dm 644 src/* -t "${pkgdir}/usr/src/googletest/src"
  install -Dm 644 CMakeLists.txt -t "${pkgdir}/usr/src/googletest"

  cd ../googlemock
  install -Dm 644 cmake/* -t "${pkgdir}/usr/src/gmock/cmake"
  install -Dm 644 src/* -t "${pkgdir}/usr/src/gmock/src"
  install -Dm 644 CMakeLists.txt -t "${pkgdir}/usr/src/gmock"

  sed -i 's|src/||' "${pkgdir}/usr/src/gmock/src/gmock-all.cc"
}
