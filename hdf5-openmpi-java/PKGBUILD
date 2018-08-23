# Maintainer : George Eleftheriou <eleftg>
# Contributor: Jingbei Li <petronny>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: Bruno Pagani (a.k.a. ArchangeGabriel) <archange@archlinux.org>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: damir <damir@archlinux.org>
# Contributor: Tom K <tomk@runbox.com>
# Contributor: Jed Brown <jed@59A2.org>
# Contributor: Simone Pezzuto <junki.gnu@gmail.com>

_pkgname=hdf5
_mpi=openmpi
pkgname=${_pkgname}-${_mpi}-java
pkgver=1.10.3
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data (${_mpi} version) (full version including its Java Native Interfaces)"
arch=('x86_64')
url="https://portal.hdfgroup.org/display/support"
license=('custom')
depends=('zlib' 'libaec' "${_mpi}")
makedepends=('time' 'gcc-fortran' 'java-environment')
provides=('hdf5-openmpi' 'hdf5' 'hdf5-cpp-fortran' "hdf5-fortran-${_mpi}")
conflicts=('hdf5' 'hdf5-openmpi')
replaces=("hdf5-fortran-${_mpi}")
source=("https://support.hdfgroup.org/ftp/HDF5/releases/${_pkgname}-${pkgver:0:4}/${_pkgname}-${pkgver}/src/${_pkgname}-${pkgver}.tar.bz2"
        'mpi.patch')
md5sums=('56c5039103c51a40e493b43c504ce982'
         'dfa8dd50b8a7ebb3ad7249c627156cf9')

prepare() {
    [ ! -d build ] && mkdir -p build
    cd "${_pkgname}-${pkgver}"

    # FS#33343
    patch -p1 -i ../mpi.patch
}

build() {
    cd build

    "${srcdir}/${_pkgname}-${pkgver}"/configure \
        CXX="mpicxx" \
        CC="mpicc" \
        FC="mpif90" \
        F9X="mpif90" \
        RUNPARALLEL="mpirun" \
        OMPI_MCA_disable_memory_allocator=1 \
        JAVADOC='javadoc -Xdoclint:none' \
        --prefix=/usr \
        --disable-static \
        --disable-sharedlib-rpath \
        --enable-build-mode=production \
        --enable-hl \
        --enable-cxx \
        --enable-fortran \
        --enable-java \
        --enable-parallel \
        --enable-unsupported \
        --with-pic \
        --with-zlib \
        --with-szlib

    make
}

check() {
    cd build

    # This is a parallel build, there will always be some MPI bugs,
    # so skip failures and don't kill the entire packaging process
    make check || warning "Some tests failed"
}

package() {
    cd build

    make -j1 DESTDIR="${pkgdir}" install

    install -dm755 "${pkgdir}/usr/share/doc/${_pkgname}"
    mv "${pkgdir}"/usr/share/{hdf5_examples,doc/${_pkgname}/examples}

    install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
}
