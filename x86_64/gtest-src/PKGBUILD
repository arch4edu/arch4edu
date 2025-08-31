# Maintainer: Kino <cybao292261@163.com>

pkgname=gtest-src
pkgver=1.17.0
pkgrel=1
pkgdesc='Google Test Source - C++ testing utility'
url='https://github.com/google/googletest'
arch=('x86_64')
license=('BSD-3-Clause')
depends=("gtest")
_srcname=googletest-${pkgver}
source=("${_srcname}.tar.gz::https://github.com/google/googletest/archive/v${pkgver}.tar.gz"
  "https://github.com/google/googletest/pull/4539.patch")
sha512sums=('0f57e9ef06925e5b7722df1eb92ef5850e8dce79220ea16a8aaff586a71c0b01460ef1713649ee24ffedb2e6ad5a51e9198c5a5ae1b2789e43feb1f494e7d45c'
            'b1130b7846f94db88ca57fd924c79d68579794e215e8dfeeb137a50639f58e53be1f9db003b05e8c703232175c46c23fb318d04623779322a741d2e197fbdd2a')
b2sums=('194df0cbe44905b9748c3df75ce3e91f0b11d766c845a11a9b86bb65249d21448b6eac1c2ea9fc3c189105f173d2330af5d0622b051f712dbf661ba5917bc96b'
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
