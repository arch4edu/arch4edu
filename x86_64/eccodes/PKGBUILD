# Maintainer: "Jan Kohnert <bughunter@jan-kohnert.de"
# Contributor: Graziano Giuliani <graziano.giuliani@poste.it>
pkgname=eccodes
pkgver=2.46.0
_attnum=45757960
pkgrel=2
pkgdesc="ECMWF decoding library for GRIB, BUFR and GTS"
arch=("i686" "x86_64")
url="https://confluence.ecmwf.int/display/ECC/ecCodes+Home"
license=("Apache-2.0")
depends=("glibc" "libaec" "libgcc" "libgfortran" "libpng" "libstdc++" "openjpeg2" "netcdf")
makedepends=("gcc-fortran" "cmake")
optdepends=("bash" "ksh")
conflicts=("grib_api" "libbufr-ecmwf")
source=(
    "${pkgname}-${pkgver}-Source.tar.gz::https://confluence.ecmwf.int/download/attachments/${_attnum}/${pkgname}-${pkgver}-Source.tar.gz?api=v2"
)
sha512sums=(
    "732ab0f23f3b56681fc103c8f8bb49ae46b06d4278c8cf0cddd99731b4bc2101910e161a3fd1b6bffeaa968d72c2e2de8ab0a9c33c23025e554302fb084d167a"
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
    -D CMAKE_BUILD_TYPE=None
    -D CMAKE_INSTALL_PREFIX=/usr
    -D CMAKE_INSTALL_DATADIR=/usr/share
    -D CMAKE_INSTALL_DATAROOTDIR="/usr/share/$pkgname/definitions"
    -D ENABLE_AEC=ON
    -D ENABLE_ECCODES_THREADS=ON
    # since we skipped downloading the test-data file, this will download necessary data on-the-fly when testing
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
