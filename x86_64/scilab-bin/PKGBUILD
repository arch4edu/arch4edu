# Maintainer: envolution
# Contributor: David Garfias <dgarfiasme@gmail.com>
# Contributor: ffcc <ffercc at gmail dot com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Marcel Hasler <mahasler at gmail dot com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=scilab-bin
_pkgname=${pkgname%-bin}
pkgver=2026.0.0
pkgrel=1
pkgdesc="a powerful computing environment for engineering and scientific applications."
arch=("x86_64")
license=("GPL-2.0-or-later")
url="https://www.scilab.org"
# Standalone package
depends=(
  ncurses5-compat-libs
  hicolor-icon-theme
  freetype2
  zlib
  ruby
  alsa-lib
  cairo
  pango
  dbus
  libxrandr
  libx11
  libxi
  libxext
  nss
  libdrm
  java-runtime
  python
  libxtst
  nspr
  libxkbcommon
  libxxf86vm
  libcups
  glib2
  libxdamage
  libxcursor
  libxrender
  libxcb
  libxcomposite
  expat
  mesa
  perl
  libxfixes
  at-spi2-core)
conflicts=(scilab)
provides=(scilab)
options=(!strip)
# From Scilab downloads page (https://www.scilab.org/download/)
source=("https://www.scilab.org/download/${pkgver}/${_pkgname}-${pkgver}.bin.${CARCH}-linux-gnu.tar.xz")
sha256sums=('800b5a8f5c1e4e1ced1618e245b7e6a9d420d1732ab94e8b5f913f05e1be8a57')

package() {
  install -d "${pkgdir}/opt"
  mkdir -p "${pkgdir}/usr/bin"
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${pkgdir}/opt/${_pkgname}"
  ln -s "/usr/lib/jvm/java-8-openjdk/jre" "${pkgdir}/opt/${_pkgname}/thirdparty/java"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  install -Dm 644 COPYING "${pkgdir}/usr/share/licenses/${_pkgname}/COPYING"
  install -d "${pkgdir}/usr/share/applications"
  install -Dm 644 share/applications/*.desktop "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons"
  cp -a share/icons/hicolor "${pkgdir}/usr/share/icons"
  for _executable in scilab scilab-cli scilab-adv-cli scinotes xcos; do
    ln -s "${instdir}/opt/scilab/bin/${_executable}" "${pkgdir}/usr/bin/${_executable}"
  done
}

# vim: ts=2 sw=2 et:
# vim:set ts=2 sw=2 et:
