# Maintainer: Exos  <exos at kaktheplanet dot xyz>

pkgname=openctm-tools
pkgver=1.0.3
pkgrel=2
epoch=2
pkgdesc="Open Compressed Triangle Mesh file format"
arch=('x86_64' 'aarch64')
url="https://sourceforge.net/projects/openctm"
license=('zlib')
depends=('gtk2-compat' 'glu' 'glut')
makedepends=()
source=(
    "${pkgname}-${pkgver}::https://downloads.sourceforge.net/project/openctm/OpenCTM-${pkgver}/OpenCTM-${pkgver}-src.tar.bz2"
    "OpenCTM-$pkgver.patch"
)
sha512sums=(
    'fdfa08d19ecbfea99ba01aa2032e941ed6313394a96bd69f8984c2d2d079d836c616471d2bdf6f40175e75659f3ad0ba41502bc3d8224091472f40893ea8746e'
    '4e15479bc95e8b82977ca1adff2d6a4b4d81e99d83bc0b66933c035cd54fb97807d2a3ff9981cfca505f46b1c2027005199330b26da5494fa97ab022b4e4a0b3'
)

prepare() {
    # Patch g++ command, see
    # https://stackoverflow.com/questions/23729213/link-error-when-trying-to-build-a-simple-opengl-program
    cd "OpenCTM-${pkgver}"
    patch --forward --strip=1 --input="${srcdir}/OpenCTM-${pkgver}.patch"
}

build() {
    cd "OpenCTM-${pkgver}"
    make -f Makefile.linux
}

package() {
    cd "OpenCTM-${pkgver}"

    O_LIBDIR=/usr/lib/
    O_INCDIR=/usr/include/
    O_BINDIR=/usr/bin/
    O_MAN1DIR=/usr/share/man/man1/

    mkdir -p "${pkgdir}/usr/"{lib,include,bin,share/man/man1}

    make LIBDIR="${pkgdir}/${O_LIBDIR}" \
         INCDIR="${pkgdir}/${O_INCDIR}" \
         BINDIR="${pkgdir}/${O_BINDIR}" \
         MAN1DIR="${pkgdir}/${O_MAN1DIR}" \
         -f Makefile.linux install
}
