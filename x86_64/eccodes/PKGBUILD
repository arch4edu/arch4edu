# Maintainer: "Jan Kohnert <bughunter@jan-kohnert.de"
# Contributor: Graziano Giuliani <graziano.giuliani@poste.it>
pkgname=eccodes
pkgver=2.33.0
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
    "4afc2a9e59da54093eb318a1447904faac7371df980a57ce21e04ef98d1d7e02f10ef363a497d29f086b1f17a86ba4e46bf14898cd227eae8bbe0297c62b4183"
    "c495a71f18ea01aa480b0920fbfce8d370574d412c95eb04823d0d4544fed0e2dba8e98d63e2be0a3c33a127840e7262d391373fab9304a773e9764457ade5a7"
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
