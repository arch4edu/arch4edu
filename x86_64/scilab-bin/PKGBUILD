# Maintainer: David Garfias <jose.garfias@ingenieria.unam.edu> 
# Contributor: ffcc <ffercc at gmail dot com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Marcel Hasler <mahasler at gmail dot com>

pkgname=scilab-bin
_pkgname=${pkgname%-bin}
pkgver=2023.0.0
pkgrel=1
pkgdesc="A software package for numerical computation, providing a powerful computing environment for engineering and scientific applications."
arch=("x86_64")
license=("GPL")
url="https://www.scilab.org"
# Standalone package
depends=('ncurses5-compat-libs' 'jre8-openjdk')
conflicts=('scilab' 'scilab-git')
provides=('scilab')
options=(!strip)
# From Scilab downloads page (https://www.scilab.org/download/)
source=("https://www.scilab.org/download/${pkgver}/${_pkgname}-${pkgver}.bin.x86_64-pc-linux-gnu.tar.xz")
sha256sums=("1278955d3bfc4b5be9290ec17f40b9e79789dee09be6893ba83f382e89015a66")

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  rm -R thirdparty/java
}

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
