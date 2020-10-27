# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=stepcode
pkgver=0.8
pkgrel=4
pkgdesc="Data exchange with ISO 10303. Used with IFC, STEP, and other standards
to exchange data wit C++ and Python."
arch=('i686' 'x86_64')
url="https://stepcode.github.io"
license=('BSD 3-Clause')
depends=('gcc')
makedepends=('cmake')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/stepcode/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('f9cc8a5a4193f97add595c1909433154f82983b892c532be2a696758b153fd2c')

build() {
	mkdir -p "${srcdir}/${pkgname}-${pkgver}/build"
	cd "${srcdir}/${pkgname}-${pkgver}/build"

	cmake .. \
        -DSC_IS_SUBBUILD=false \
        -DSC_BUILD_TYPE=Release \
		-DSC_INSTALL_PREFIX="/usr"

	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}/build"
	make DESTDIR="${pkgdir}/" install
}
