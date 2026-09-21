# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: Robert Walaski <robert@walaski.cz>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=153.0.8010.52
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://storage.googleapis.com/chrome-for-testing-public/${pkgver}/linux64/${pkgname}-linux64.zip")
sha512sums=('c6f5830bcb2d69b73f97bea3eb59f250cf525f409f40be95ae5c4ec96a68007aed94b5849cd40f0fe0b02ec08a754f8c74ed3d7b700ea825078ea2415b8b67f3')
package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname-linux64/$pkgname"
}
