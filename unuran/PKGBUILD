# Maintainer: Konstantin Gizdov <arch at kge dot pw>

pkgname=unuran
pkgver=1.8.1
pkgrel=1
provides=('unuran')
pkgdesc='A C library for generating non-uniform pseudorandom variates.'
arch=('i686' 'x86_64')
url='http://statmath.wu.ac.at/unuran/'
license=('GPL2')
makedepends=('make')
depends=('gsl')
options=('!emptydirs')
source=("http://statmath.wu.ac.at/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('c270ae96857857dbac6450043df865e0517f52856ddbe5202fd35583b13c5193')
prepare(){
    cd ${pkgname}-${pkgver}

    ./configure --prefix=/usr --with-urng-gsl --enable-shared
}

build() {
    cd ${pkgname}-${pkgver}

    make ${MAKEFLAGS}
}

package() {
    cd ${pkgname}-${pkgver}

    make DESTDIR=${pkgdir} install
}
