# Maintainer: Michael Lass <bevan@bi-co.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=archlinux-java-run
pkgver=12
pkgrel=1
pkgdesc="Java Application Launcher for Arch Linux"
arch=(any)
url="https://github.com/michaellass/archlinux-java-run"
license=('MIT')
depends=(bash java-runtime-common)
source=(https://github.com/michaellass/${pkgname}/archive/v${pkgver}.tar.gz)
sha256sums=('de935ee8aaae3e59d619c96deab6d126a11e994e498634760952b83a1b9da2dc')

package() {
  cd  "${srcdir}/${pkgname}-${pkgver}"
  make PREFIX=/usr DESTDIR="${pkgdir}" install
}
