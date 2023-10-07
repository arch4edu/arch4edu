# Maintainer: "Jan Kohnert <bughunter@jan-kohnert.de"
# Contributor: Graziano Giuliani <graziano.giuliani@poste.it>
pkgname=eccodes
pkgver=2.32.0
_attnum=45757960
pkgrel=1
pkgdesc="ECMWF decoding library for GRIB, BUFR and GTS"
arch=("i686" "x86_64")
url="https://confluence.ecmwf.int/display/ECC/ecCodes+Home"
license=("Apache")
depends=("glibc" "gcc-libs" "libaec" "libpng" "openjpeg2" "netcdf")
makedepends=("gcc-fortran" "cmake")
optdepends=("bash" "ksh")
conflicts=("grib_api" "libbufr-ecmwf")
source=(
    "${pkgname}-${pkgver}-Source.tar.gz::https://confluence.ecmwf.int/download/attachments/${_attnum}/${pkgname}-${pkgver}-Source.tar.gz?api=v2"
    "${pkgname}-${pkgver}-test-data.tar.gz::https://get.ecmwf.int/repository/test-data/eccodes/eccodes_test_data.tar.gz"
)
sha512sums=(
    "30b867b396c13cc7f0a8049b4c5e938a634a3e90d1e8835923a068b645ac3f4ec43df30ecb0dcd6e29aaf81a0e40cbbf75c49f6172109def26e6ec330ce4ed9f"
    "0457878caad6a3395daf60e27cfb72121526065b0cf4da144c7499b8d38bebae0952ddbd20ef0eb53fad77ada60160039340da01001f19fbb7fb1ccbb3d0547a"
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
