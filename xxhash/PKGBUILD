# Maintainer: Fabien Dubosson <fabien dot dubosson at gmail dot com>
# Co-maintainer: Konstantin Gizdov <arch at kge dot com>

pkgname=xxhash
_pkgname=xxHash
pkgver=0.6.5
pkgrel=1
pkgdesc='Extremely fast non-cryptographic hash algorithm'
url='http://www.xxhash.com/'
license=('GPL2' 'BSD')
arch=('i686' 'x86_64')
conflicts=('libxxhash')
changelog='changelog'
source=("https://github.com/Cyan4973/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('19030315f4fc1b4b2cdb9d7a317069a109f90e39d1fe4c9159b7aaa39030eb95')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    make PREFIX=/usr V=1 XXH_INLINE_ALL=1 XXH_PRIVATE_API=1 XXH_NAMESPACE=1
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

    make PREFIX=/usr DESTDIR="${pkgdir}" install
}

# vim:set ts=4 sw=4 et:
