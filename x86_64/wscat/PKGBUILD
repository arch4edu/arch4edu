# Maintainer: Arturo Penen <apenen@gmail.com>
_pkgname=wscat
pkgname="$_pkgname"
pkgver=5.2.0
pkgrel=2
pkgdesc="Netcat-like utility for WebSockets"
url="https://github.com/websockets/wscat"
arch=("x86_64" "i686")
license=("MIT")
source=("https://registry.npmjs.org/$_pkgname/-/$_pkgname-$pkgver.tgz")
noextract=("${_pkgname}-${pkgver}.tgz")
sha256sums=('e8c4bb9bc66a2303c0e6a3f2cf2a0cc04ec29ccca8ae0371eda499e3811717a8')
depends=("nodejs")
makedepends=("npm")

package() {
    npm install -g --cache "${srcdir}/npm-cache" --prefix "${pkgdir}/usr" "${srcdir}/${_pkgname}-${pkgver}.tgz"

    # npm gives ownership of ALL FILES to build user
    # https://bugs.archlinux.org/task/63396
    chown -R root:root "${pkgdir}"
}
