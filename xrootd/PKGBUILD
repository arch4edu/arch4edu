# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
# Contributor: Alex Pearce < alex at alexpearce dot me >
pkgname=xrootd
pkgver=4.8.2
pkgrel=1
pkgdesc="Software framework for fast, low latency, scalable and fault tolerant data access."
provides=('xrootd' 'xrootd-abi0')
arch=('i686' 'x86_64')
url="http://xrootd.org/"
license=('LGPL3')
depends=('ceph' 'libxml2')
makedepends=('cmake')
options=('!emptydirs')
source=("http://xrootd.org/download/v${pkgver}/xrootd-${pkgver}.tar.gz")
sha256sums=('8f28ec53e799d4aa55bd0cc4ab278d9762e0e57ac40a4b02af7fc53dcd1bef39')

prepare() {
    rm -rf "${srcdir}/build"
    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"

    cmake "${srcdir}/${pkgname}-${pkgver}" \
          -DCMAKE_BUILD_TYPE:STRING=Release \
          -DCMAKE_INSTALL_LIBDIR:PATH=lib \
          -DCMAKE_INSTALL_PREFIX:PATH=/usr
          # Currently Python3 is incompatible
          # -DXRD_PYTHON_REQ_VERSION=$( python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))' )
}

build() {
    cd "${srcdir}/build"
    make ${MAKEFLAGS}
}

package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}" install
}
