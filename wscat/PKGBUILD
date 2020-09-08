# Maintainer: Arturo Penen <apenen@gmail.com>
pkgname=wscat
pkgver=4.0.1
pkgrel=2
pkgdesc="Netcat-like utility for WebSockets"
url="https://github.com/websockets/wscat"
arch=("x86_64" "i686")
license=("MIT")
depends=("nodejs")
makedepends=("npm")

package() {
    export npm_config_prefix="${pkgdir}/usr"
    npm install -g wscat@${pkgver}
}
