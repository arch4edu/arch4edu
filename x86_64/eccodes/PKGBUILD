# Maintainer: "Jan Kohnert <bughunter@jan-kohnert.de"
# Contributor: Graziano Giuliani <graziano.giuliani@poste.it>
pkgname=eccodes
pkgver=2.32.1
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
    "7fdb34cee0b656ebbecc04d654642b0524eb6e772c1d811471061698f4ec2d31da3be3d66ee697dd3e106f3e8024058b4c165c6dad59868af66a38949c956c77"
    "86767a308841849c7ece006e9f6c68123dc07d8640b038e25529b91ab495d3f10ad5356e9100ef238de6756c67917be13a676f4ab0708fb381021c746e00183e"
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
