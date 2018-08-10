# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
# Contributor: Alex Pearce < alex at alexpearce dot me >
pkgname=xrootd
pkgver=4.8.4
pkgrel=1
pkgdesc="Software framework for fast, low latency, scalable and fault tolerant data access."
provides=('xrootd' 'xrootd-abi0')
arch=('i686' 'x86_64')
url="http://xrootd.org/"
license=('LGPL3')
depends=('ceph' 'libxml2' 'python')
makedepends=('cmake')
options=('!emptydirs')
source=("http://xrootd.org/download/v${pkgver}/xrootd-${pkgver}.tar.gz"
        'fix_buffer_overflow.patch')
sha256sums=('f148d55b16525567c0f893edf9bb2975f7c09f87f0599463e19e1b456a9d95ba'
            'd52b193d3e8c96064f2d151484abd433dd47835cfe0031b31bcfab2c17b69b85')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -p1 -i "${srcdir}/fix_buffer_overflow.patch"

    rm -rf "${srcdir}/build"
    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"

    CFLAGS="${CFLAGS} -pthread" \
    CXXFLAGS="${CXXFLAGS} -pthread" \
    LDFLAGS="${LDFLAGS} -pthread -Wl,--no-undefined" \
    cmake "${srcdir}/${pkgname}-${pkgver}" \
          -DCMAKE_BUILD_TYPE:STRING=Release \
          -DCMAKE_INSTALL_LIBDIR:PATH=lib \
          -DCMAKE_INSTALL_PREFIX:PATH=/usr \
          -DXRD_PYTHON_REQ_VERSION=$( python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))' )
}

build() {
    cd "${srcdir}/build"
    make ${MAKEFLAGS}
}

package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}" install
}
