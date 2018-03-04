# $Id$
# Maintainer : George Eleftheriou <eleftg>
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
pkgver=1.10.1
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data (${_mpi} version) (full version including its Java Native Interfaces)"
arch=('i686' 'x86_64')
url="https://www.hdfgroup.org/HDF5/"
license=('custom')
depends=('zlib' 'openmpi')
makedepends=('time' 'gcc-fortran' 'java-environment')
provides=('hdf5-openmpi' 'hdf5' 'hdf5-cpp-fortran' "hdf5-fortran-${_mpi}")
conflicts=('hdf5' 'hdf5-openmpi')
replaces=("hdf5-fortran-${_mpi}")
source=("https://support.hdfgroup.org/ftp/HDF5/releases/${_pkgname}-${pkgver:0:4}/${_pkgname}-${pkgver/_/-}/src/${_pkgname}-${pkgver/_/-}.tar.bz2"
        'mpi.patch')
md5sums=('d89893c05ee7ea8611b51bb39450d64e'
         'dfa8dd50b8a7ebb3ad7249c627156cf9')

prepare() {
    cd ${_pkgname}-${pkgver/_/-}

    # FS#33343
    patch -p1 -i ../mpi.patch
}

build() {
    cd ${_pkgname}-${pkgver/_/-}
    ./configure \
        CXX="mpicxx" \
        CC="mpicc" \
        FC="mpif90" \
        F9X="mpif90" \
        RUNPARALLEL="mpirun" \
        OMPI_MCA_disable_memory_allocator=1 \
        --prefix=/usr \
        --disable-static \
        --enable-hl \
        --enable-build-mode=production \
        --with-pic \
        --docdir=/usr/share/doc/hdf5/ \
        --disable-sharedlib-rpath \
        --enable-cxx \
        --enable-fortran \
        --enable-fortran2003 \
        --enable-java \
        --enable-parallel \
        --enable-unsupported \
        --with-zlib
    make
}

package() {
    cd ${_pkgname}-${pkgver/_/-}

    make -j1 DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}"/usr/lib/libdynlib*.so

    install -dm755 "${pkgdir}"/usr/share/${_pkgname}
    mv "${pkgdir}"/usr/share/{hdf5_examples,${_pkgname}/examples}

    install -Dm644 COPYING "${pkgdir}"/usr/share/licenses/${_pkgname}/LICENSE
}
