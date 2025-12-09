# Maintainer: Arturo Penen <apenen@gmail.com>
_pkgname=wscat
pkgname="$_pkgname"
pkgver=6.1.0
pkgrel=1
pkgdesc="Netcat-like utility for WebSockets"
url="https://github.com/websockets/wscat"
arch=("x86_64" "i686")
license=("MIT")
source=("https://registry.npmjs.org/$_pkgname/-/$_pkgname-$pkgver.tgz")
noextract=("${_pkgname}-${pkgver}.tgz")
sha256sums=('4867c77c19469e63f02835f31d2321d1ff0a12b987bf5b0314bc69dff5e15e1e')
depends=("nodejs")
makedepends=("npm")

package() {
    npm install -g --cache "${srcdir}/npm-cache" --prefix "${pkgdir}/usr" "${srcdir}/${_pkgname}-${pkgver}.tgz"

    # npm gives ownership of ALL FILES to build user
    # https://bugs.archlinux.org/task/63396
    chown -R root:root "${pkgdir}"
}
