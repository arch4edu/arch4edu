# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: Robert Walaski <robert@walaski.cz>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=149.0.7827.22
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://storage.googleapis.com/chrome-for-testing-public/${pkgver}/linux64/${pkgname}-linux64.zip")
sha512sums=('759e90b7ee88d2b143f3799459790c762aa6701201aa566bc468d2fd908204311bb9d7ae5cdb6d1d741e342da786d8d9665c13ccd22fa98b3d0d96cc4c0ca60e')
package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname-linux64/$pkgname"
}
