# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>

pkgname=fakepkg
pkgver=1.42.2
pkgrel=1
pkgdesc="Tool to reassemble installed packages from its deliverd files. It comes in handy if there is no internet connection available and you have no access to an up-to-date package cache"
arch=('any')
license=('GPL2')
url="https://github.com/Edenhofer/fakepkg"
depends=('bash>=4.2' 'pacman' 'tar' 'gzip' 'sed' 'awk')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/Edenhofer/fakepkg/archive/v${pkgver}.tar.gz")
sha512sums=('fca6bfd7a926e86cfa204c00f2885b76ca57f2159f5fbb17b3b02321c354a42dde027408449bb73991f15538856a0f2c159381e0c54451fcfa3eebf8fceb0f17')

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	install -D -m755 "${pkgname}"       "${pkgdir}/usr/bin/${pkgname}"
	install -D -m644 "man/${pkgname}.1" "${pkgdir}/usr/share/man/man1/${pkgname}.1"
}
