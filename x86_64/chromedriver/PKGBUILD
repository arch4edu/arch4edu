# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: Robert Walaski <robert@walaski.cz>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=129.0.6668.70
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://storage.googleapis.com/chrome-for-testing-public/${pkgver}/linux64/${pkgname}-linux64.zip")
sha512sums=('64edfc3d79a03db6fa9a5f16e7139d2102a8b3ab11ca2dc143b0b2c4d1dd87226038a9b049f0ecf930c074e49deb303d57c2680f650f5312d9d37d0f470e8f9f')
package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname-linux64/$pkgname"
}
