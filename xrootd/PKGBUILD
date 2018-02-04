# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
# Contributor: Alex Pearce < alex at alexpearce dot me >
pkgname=xrootd
pkgver=4.8.1
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
sha256sums=('edee2673d941daf7a6e5c963d339d4a69b4db5c4b6f77b4548b3129b42198029')

prepare() {
    # cd "${srcdir}/${pkgname}-${pkgver}"
    # patch -p1 -i "${srcdir}/gcc7.patch"

    rm -rf "${srcdir}/build"
    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"

    msg2 'Configuring...'
    cmake "${srcdir}/${pkgname}-${pkgver}" \
          -DCMAKE_BUILD_TYPE:STRING=Release \
          -DCMAKE_INSTALL_LIBDIR:PATH=lib \
          -DCMAKE_INSTALL_PREFIX:PATH=/usr
          # Currently Python3 is incompatible
          # -DXRD_PYTHON_REQ_VERSION=$( python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))' )
}

build() {
    msg2 'Compiling...'
    cd "${srcdir}/build"
    make ${MAKEFLAGS}
}

package() {
    cd "${srcdir}/build"
    msg2 'Installing...'
    make DESTDIR="${pkgdir}" install
}
