# Maintainer: Bian Jiaping <ssbianjp@gmail.com>
# Contributor : farseerfc <farseerfc@archlinuxcn.org>
# Contributor : Fernando "Firef0x" G.P. da Silva <firefgx { aT ) gmail [ d0t } com>
# Contributor : Sander Boom <sander at inflowmotion dot nl> (From sublime-text-dev)
# Contributor : realitygaps <realitygaps at yahoo dot com> (From sublime-text-dev)
# Contributor : ska <skatiger (at} gmail {dot) com> (From sublime-text-imfix)

pkgname=sublime-text-dev-imfix
pkgver=3.3180
pkgrel=1
pkgdesc="Sophisticated text editor for code, markup and prose - Dev build with input method support for CJK users"
arch=('i686' 'x86_64')
url="https://www.sublimetext.com/3dev"
license=('custom')
depends=('libpng' 'gtk2')
conflicts=('sublime-text' 'sublime-text-dev' 'sublime-text-nightly')
provides=('sublime-text' 'sublime-text-dev' 'sublime-text-nightly')

validpgpkeys=("1EDDE2CDFC025D17F6DA9EC0ADAE6AD28A8F901A")

source=('subl' 'sublime_imfix.c')
source_i686=(
  "https://download.sublimetext.com/sublime_text_3_build_${pkgver:2}_x32.tar.bz2.asc"
  "https://download.sublimetext.com/sublime_text_3_build_${pkgver:2}_x32.tar.bz2"
)
source_x86_64=(
  "https://download.sublimetext.com/sublime_text_3_build_${pkgver:2}_x64.tar.bz2.asc"
  "https://download.sublimetext.com/sublime_text_3_build_${pkgver:2}_x64.tar.bz2"
)

sha256sums=('1ec8b8212e70cbe8612048ec039402cee044527507e72d8020c551ebbd5b2789'
            '5903b47f7dfbf079987c566361c5735a002dcbf25d0f86de86b7dce424f36700'
           )

sha256sums_x86_64=('SKIP' 'SKIP')
sha256sums_i686=('SKIP' 'SKIP')

build() {
  # build imfix library
  gcc -shared -o libsublime-imfix.so $(pkg-config --libs --cflags gtk+-2.0) -fPIC sublime_imfix.c
}

package() {
  cd "${srcdir}"

  install -dm755 "${pkgdir}/opt"
  cp --preserve=mode -r "sublime_text_3" "${pkgdir}/opt/sublime_text"

  # Install imfix library
  install -Dm755 libsublime-imfix.so "${pkgdir}/opt/sublime_text/libsublime-imfix.so"

  for res in 16x16 32x32 48x48 128x128 256x256; do
    install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
    ln -s "/opt/sublime_text/Icon/${res}/sublime-text.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime-text.png"
  done

  install -dm755 "${pkgdir}/usr/share/applications"
  install -Dm644 "sublime_text_3/sublime_text.desktop" "${pkgdir}/usr/share/applications/sublime_text.desktop"
  sed -i 's#/opt/sublime_text/sublime_text#subl#g' "${pkgdir}/usr/share/applications/sublime_text.desktop"
  install -Dm755 subl "${pkgdir}/usr/bin/subl"
  ln -s /opt/sublime_text/sublime_text "${pkgdir}/usr/bin/subl-noimfix"
}
