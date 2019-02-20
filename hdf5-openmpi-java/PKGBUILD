# Maintainer : George Eleftheriou <eleftg>
# Contributor: Martin Diehl <MartinDiehl>
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
_prefix=/usr
pkgver=1.10.4
pkgrel=3
pkgdesc="General purpose library and file format for storing scientific data (${_mpi} version) (full version including its Java Native Interfaces)"
arch=('x86_64')
url="https://portal.hdfgroup.org/display/support"
license=('custom')
depends=('bash' 'libaec' "${_mpi}")
makedepends=('cmake' 'time' 'java-environment' 'gcc-fortran')
options=('staticlibs')
provides=('hdf5-java' 'hdf5-openmpi' 'hdf5' 'hdf5-cpp-fortran' "hdf5-fortran-${_mpi}")
conflicts=('hdf5-java' 'hdf5' 'hdf5-openmpi')
replaces=("hdf5-fortran-${_mpi}")
source=("https://support.hdfgroup.org/ftp/HDF5/releases/${_pkgname}-${pkgver:0:4}/${_pkgname}-${pkgver}/src/${_pkgname}-${pkgver}.tar.bz2"
        'mpi.patch'
        'mpi4.patch')
md5sums=('886148d0cc9ffd3c8e1fce0bd75ed07b'
         '63b43e3d4a5bbea4bcecc84874e08913'
         '5b981fb1c802d5cacd46af23162ff410')

prepare() {
    mkdir -p build
    cd "${_pkgname}-${pkgver}"

    # FS#33343
    patch -p1 -i ../mpi.patch

    # patch for MPI4 compatibility
    patch -p1 -i ../mpi4.patch
}

build() {
    cd build

    # Crazy workaround: run CMake to generate pkg-config file
    RUNPARALLEL="mpirun" \
    OMPI_MCA_disable_memory_allocator=1 \
    JAVADOC='javadoc -Xdoclint:none' \
    cmake ../${_pkgname}-${pkgver}  \
        -DCMAKE_CXX_COMPILER=mpicxx \
        -DCMAKE_C_COMPILER=mpicc \
        -DCMAKE_Fortran_COMPILER=mpif90 \
        -DCMAKE_C_FLAGS="${CPPFLAGS} ${CFLAGS}" \
        -DCMAKE_CXX_FLAGS="${CPPFLAGS} ${CXXFLAGS}" \
        -DCMAKE_EXE_LINKER_FLAGS="${LDFLAGS}" \
        -DCMAKE_SHARED_LINKER_FLAGS="${LDFLAGS}" \
        -DCMAKE_MODULE_LINKER_FLAGS="${LDFLAGS}" \
        -DCMAKE_INSTALL_RPATH="" \
        -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX="${_prefix}" \
        -DALLOW_UNSUPPORTED=ON \
        -DHDF5_BUILD_HL_LIB=ON \
        -DHDF5_BUILD_CPP_LIB=ON \
        -DHDF5_BUILD_FORTRAN=ON \
        -DHDF5_BUILD_JAVA=ON \
        -DHDF5_ENABLE_Z_LIB_SUPPORT=ON \
        -DHDF5_ENABLE_SZIP_SUPPORT=ON \
        -DHDF5_ENABLE_SZIP_ENCODING=ON \
        -DHDF5_ENABLE_PARALLEL=ON \
        -DBUILD_TESTING=OFF

    # But don’t build with it, it’s quite broken
    "${srcdir}/${_pkgname}-${pkgver}"/configure \
        CXX="mpicxx" \
        CC="mpicc" \
        FC="mpif90" \
        F9X="mpif90" \
        RUNPARALLEL="mpirun" \
        OMPI_MCA_disable_memory_allocator=1 \
        JAVADOC='javadoc -Xdoclint:none' \
        --prefix="${_prefix}" \
        --docdir="${_prefix}/share/doc/${_pkgname}" \
        --enable-static \
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

package() {
    cd build

    make DESTDIR="${pkgdir}" install

    # Remove leftover test files
    rm "${pkgdir}${_prefix}"/include/tst{ds,image,lite,table}{,_tests}.mod

    # Move examples to a proper place
    install -dm755 "${pkgdir}${_prefix}/share/doc/${_pkgname}"
    mv "${pkgdir}${_prefix}"/share/{hdf5_examples,doc/${_pkgname}/examples}

    install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/COPYING" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    install -Dm644 CMakeFiles/hdf5{,_hl}{,_cpp}-${pkgver}.pc \
        -t "${pkgdir}${_prefix}"/lib/pkgconfig
}
