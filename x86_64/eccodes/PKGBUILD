# Maintainer: "Jan Kohnert <bughunter@jan-kohnert.de"
# Contributor: Graziano Giuliani <graziano.giuliani@poste.it>
pkgname=eccodes
pkgver=2.36.0
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
    "c18df75593af6461dfa64d717ec5a6af9492bc5a851b87f13ca759343abfbf21ec6e3e5978654f95641e86429b9b105bceb9414f8d925275d2a1b305441905d0"
    "2e09211268eaac27f93468d8d27b7ea40595fc77fa2db35a530bad347a9e4391722d65c533b4d42dd7cde6a2b10fc1bfd5d986d0f5cddc8b7f738f69dd9df039"
)
    
prepare() {
    mkdir -p "$srcdir/${pkgname}-${pkgver}-Source/build"
    if [ -d "$srcdir/${pkgname}-${pkgver}-Source/build/data" ]; then
        rm -r "$srcdir/${pkgname}-${pkgver}-Source/build/data"
    fi
    mv data "$srcdir/${pkgname}-${pkgver}-Source/build/"
}

build() {
    cd "$srcdir/${pkgname}-${pkgver}-Source/build"
    cmake -DCMAKE_BUILD_TYPE=production -DCMAKE_INSTALL_DATADIR=/usr/share \
        -DCMAKE_INSTALL_DATAROOTDIR=/usr/share/$pkgname/definitions \
        -DCMAKE_INSTALL_PREFIX=/usr -DENABLE_AEC=ON \
        -DENABLE_ECCODES_THREADS=ON -DENABLE_EXTRA_TESTS=ON -DENABLE_JPG=ON \
        -DENABLE_JPG_LIBJASPER=OFF -DENABLE_JPG_LIBOPENJPEG=ON -DENABLE_PNG=ON ..
    make
}

check() {
    cd "$srcdir/${pkgname}-${pkgver}-Source/build"
    make test
}

package() {
    cd "$srcdir/${pkgname}-${pkgver}-Source/build"
    make DESTDIR="$pkgdir" install
}
