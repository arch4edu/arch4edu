pkgname=wscat
pkgver=4.0.0
pkgrel=1
pkgdesc="Netcat-like utility for WebSockets"
url="https://github.com/websockets/wscat"
arch=("x86_64" "i686")
license=("custom")
depends=("nodejs")
makedepends=("npm")

pkgver() {
    npm show wscat version
}

package() {
    export npm_config_prefix="${pkgdir}/usr"
    npm install -g wscat
}
