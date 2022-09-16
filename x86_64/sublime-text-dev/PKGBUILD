# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Sander Boom <sanderboom@gmail.com>
# Contributor: realitygaps <realitygaps at yahoo dot com>

pkgname=sublime-text-dev
pkgver=4.4136
pkgrel=1
pkgdesc="Sophisticated text editor for code, html and prose - dev build"
arch=('x86_64' 'aarch64')
url="https://www.sublimetext.com/dev"
license=('custom')
depends=('libpng' 'gtk3')
optdepends=('gksu: sudo-save support')
conflicts=('sublime-text')
provides=('sublime-text')
install=${pkgname}.install

source=('sublime_text.desktop')
source_x86_64=("https://download.sublimetext.com/sublime_text_build_${pkgver:2}_x64.tar.xz")
source_aarch64=("https://download.sublimetext.com/sublime_text_build_${pkgver:2}_arm64.tar.xz")

sha256sums=('e991aac5207655dadf69c6f74c194c80009fb9767d7710337f586908969aa9cf')
sha256sums_x86_64=('e9c49a17cb1e4b75e95e9a1a44e3b9b6956ec09cc4fb3d64cf0c4d94e51a763d')
sha256sums_aarch64=('32d89bf22dbd14216eb515e658f412a7d87f15c2c3efec2ffad1808f07fd777c')

package() {
  cd "${srcdir}"

  install -dm755 "${pkgdir}/opt"
  cp --preserve=mode -r "sublime_text" "${pkgdir}/opt/sublime_text"

  for res in 128x128 16x16 256x256 32x32 48x48; do
    install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
    ln -s "/opt/sublime_text/Icon/${res}/sublime-text.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime-text.png"
  done

  install -dm755 "${pkgdir}/usr/share/applications"
  install -Dm644 "sublime_text.desktop" "${pkgdir}/usr/share/applications/sublime_text.desktop"

  install -dm755 "${pkgdir}/usr/bin"
  ln -s "/opt/sublime_text/sublime_text" "${pkgdir}/usr/bin/subl"
}
