# Maintainer: "Jan Kohnert <bughunter@jan-kohnert.de"
# Contributor: Graziano Giuliani <graziano.giuliani@poste.it>
pkgname=eccodes
pkgver=2.45.0
_attnum=45757960
pkgrel=2
pkgdesc="ECMWF decoding library for GRIB, BUFR and GTS"
arch=("i686" "x86_64")
url="https://confluence.ecmwf.int/display/ECC/ecCodes+Home"
license=("Apache-2.0")
depends=("glibc" "gcc-libs" "libaec" "libpng" "openjpeg2" "netcdf")
makedepends=("gcc-fortran" "cmake")
optdepends=("bash" "ksh")
conflicts=("grib_api" "libbufr-ecmwf")
source=(
    "${pkgname}-${pkgver}-Source.tar.gz::https://confluence.ecmwf.int/download/attachments/${_attnum}/${pkgname}-${pkgver}-Source.tar.gz?api=v2"
    "${pkgname}-${pkgver}-test-data.tar.gz::https://get.ecmwf.int/repository/test-data/eccodes/eccodes_test_data.tar.gz"
)
sha512sums=(
    "aa5f5c01ce9d551706ca8242ab6a4663b0c6bf114aa229e2aa01dba549fac1d3d57a06cf8907f18dcba4c9f1a446cbc253c3675ebf77f62ee5ac2c4fb8800dce"
    "8b4c7159dd7ed0e1e69068ec7dcabe94064f0d2abf9eac4fca2a9c730d500999e8edf1e7eeebba6fb12ae99b223c1b0843e31414538333c52f2508cb2d410151"
)

build() {
  # make sure we have a clean build environment
  if [ -d build ]; then
    rm -rf build
  fi
  local cmake_options=(
    -B build
    -S "$pkgname-$pkgver-Source"
    -W no-dev
    #-D CMAKE_BUILD_TYPE=Production
    -D CMAKE_BUILD_TYPE=None
    -D CMAKE_INSTALL_PREFIX=/usr
    -D CMAKE_INSTALL_DATADIR=/usr/share
    -D CMAKE_INSTALL_DATAROOTDIR="/usr/share/$pkgname/definitions"
    -D ENABLE_AEC=ON
    -D ENABLE_ECCODES_THREADS=ON
    -D ENABLE_EXTRA_TESTS=ON
    -D ENABLE_JPG=ON
    -D ENABLE_JPG_LIBJASPER=OFF
    -D ENABLE_JPG_LIBOPENJPEG=ON
    -D ENABLE_PNG=ON
  )
  cmake "${cmake_options[@]}"
  cmake --build build
}

check() {
  # move extra test data
  mv data ../build/
  local excluded_tests=""
  local ctest_flags=(
    --test-dir build
    # show the stdout and stderr when the test fails
    --output-on-failure
    # execute tests in parallel
    --parallel $(nproc)
    # exclude problematic tests
    --exclude-regex "$excluded_tests"
  )
  ctest "${ctest_flags[@]}"
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
