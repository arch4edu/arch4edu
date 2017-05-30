# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
pkgname=xrootd
pkgver=4.6.1
pkgrel=1
pkgdesc="Software framework for fast, low latency, scalable and fault tolerant data access."
provides=('xrootd' 'xrootd-abi0')
arch=('i686' 'x86_64')
url="http://xrootd.org/"
license=('LGPL3')
depends=('ceph' 'libxml2')
makedepends=('cmake')
options=('!emptydirs')
source=("http://xrootd.org/download/v${pkgver}/xrootd-${pkgver}.tar.gz"
        'gcc7.patch')
sha256sums=('0261ce760e8788f85d68918d7702ae30ec677a8f331dae14adc979b4cc7badf5'
            '20f4d966f302e44e4729df6454f4e12570522632a25726e38523f7fbb4b01941')
build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -p1 -i "${srcdir}/gcc7.patch"
    cd "${srcdir}"
    rm -rf "build"
    mkdir "build"
    cd "build"

    msg2 'Configuring...'
    cmake "${srcdir}/${pkgname}-${pkgver}" \
          -DCMAKE_BUILD_TYPE:STRING=Release \
          -DCMAKE_INSTALL_LIBDIR:PATH=lib \
          -DCMAKE_INSTALL_PREFIX:PATH=/usr

    msg2 'Compiling...'
    make ${MAKEFLAGS}
}

package() {
    cd "${srcdir}/build"
    msg2 'Installing...'
    make DESTDIR="${pkgdir}" install
}
