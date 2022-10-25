# Maintainer: sukanka <su975853527 at gmail.com>
# Contributor: HRKo <ootaharuki99 at gmail.com>
pkgname=mathpix-snipping-tool
pkgver=03.00.0092
pkgrel=1
pkgdesc="Mathpix Snipping Tool"
arch=('x86_64')
url="https://mathpix.com/"
license=('unknown')
depends=('qt5-x11extras' 'qt5-webengine' 'qt5-svg' 'qt5-imageformats'
)
options=(!strip)
optdepends=('wayland: Wayland support.')
source=("${pkgname}-${pkgver}-${arch}.AppImage::https://download.mathpix.com/linux/Mathpix_Snipping_Tool-${arch}.v${pkgver}.AppImage")
sha512sums=('0ea610ab2c541e7b50b4042d2912946b88f28b4345f6695ea15b40f6c84d876ce9e6c29f97b8d7f78e4a4b63a5302091d382b4e1741f43159f60bda0494a7571')


prepare() {
  cd $srcdir
  chmod a+x ${pkgname}-${pkgver}-${arch}.AppImage
  ./${pkgname}-${pkgver}-${arch}.AppImage --appimage-extract
}

package() {
  cd $srcdir/squashfs-root
  install -Dm755 usr/bin/${pkgname}     ${pkgdir}/usr/bin/${pkgname}
  install -Dm755 usr/lib/libsentry.so   ${pkgdir}/usr/lib/libsentry.so
  cp -r usr/share         ${pkgdir}/usr
  chmod 0755 -R ${pkgdir}/usr/share

  rm -rf ${pkgdir}/usr/share/doc
  # manually strip excutable here.
  strip ${pkgdir}/usr/bin/${pkgname}
}
