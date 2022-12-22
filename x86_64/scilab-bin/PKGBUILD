# Maintainer: David Garfias <jose.garfias@ingenieria.unam.edu> 
# Contributor: ffcc <ffercc at gmail dot com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Marcel Hasler <mahasler at gmail dot com>

pkgname=scilab-bin
_pkgname=${pkgname%-bin}
pkgver=6.1.1
pkgrel=5
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
source=("https://oos.eu-west-2.outscale.com/scilab-releases/${pkgver}/scilab-${pkgver}.bin.linux-x86_64.tar.gz")
sha256sums=("3ee1a7cf661d021ae26afc27b9fe50cb2d1c9c27911e5582e9d4337ebedb2c79")

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
