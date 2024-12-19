# Maintainer: sukanka <su975853527 at gmail.com>
# Contributor: HRKo <ootaharuki99 at gmail.com>
pkgname=mathpix-snipping-tool
pkgver=03.00.0128
pkgrel=1
pkgdesc="Mathpix Snipping Tool"
arch=('x86_64')
url="https://mathpix.com/"
license=('unknown')
depends=('qt5-x11extras' 'qt5-webengine' 'qt5-svg' 'qt5-imageformats' 'quazip-qt5'
)
options=(!strip)
optdepends=('wayland: Wayland support.')
source=("${pkgname}-${pkgver}-${arch}.AppImage::https://download.mathpix.com/linux/Mathpix_Snipping_Tool-${arch}.v${pkgver}.AppImage")
sha512sums=('8e9053497013195c4b37c87eac0913d05ab1a49629ca2c6c6bdea3dbd6b5a336d8d8d3fc18fca753fe31a3fe46e98c82ebac88e7dacef04d535fcf634e7bced2')


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
