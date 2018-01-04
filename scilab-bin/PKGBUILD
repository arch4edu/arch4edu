# Maintainer  : George Eleftheriou <eleftg>
# Contributor : Marcel Hasler <mahasler at gmail dot com>

pkgname=scilab-bin
_pkgname=${pkgname%-bin}
pkgver=6.0.0
pkgrel=3
pkgdesc="A software package for numerical computation, providing a powerful computing environment for engineering and scientific applications."
arch=("x86_64" "i686")
license=("BSD" "custom:CeCILL")
url="https://www.scilab.org"
# Standalone package
depends=()
conflicts=('scilab')
options=(!strip)
source_x86_64=("http://www.scilab.org/download/${pkgver}/scilab-${pkgver}.bin.linux-x86_64.tar.gz")
source_i686=("http://www.scilab.org/download/${pkgver}/scilab-${pkgver}.bin.linux-i686.tar.gz")
sha256sums_x86_64=("2d09e7ae7b7e01ef4e56fa138ebeaac78f225c3e657c569a09bfff67117de7d6")
sha256sums_i686=("c61bd5dd8f02675649e198dccb32ba7b114a254e984b48f73e7aaf8ddb8f1b52")

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}/share/applications"
  sed -i "s|Exec=scilab-adv-cli|Exec=/opt/scilab/bin/scilab-adv-cli|" scilab-adv-cli.desktop
  sed -i "s|Exec=scilab-cli|Exec=/opt/scilab/bin/scilab-cli|" scilab-cli.desktop
  sed -i "s|Exec=scilab -f|Exec=/opt/scilab/bin/scilab -f %f|" scilab.desktop
  sed -i "s|Exec=scinotes|Exec=/opt/scilab/bin/scinotes|" scinotes.desktop
  sed -i "s|Exec=xcos|Exec=/opt/scilab/bin/xcos|" xcos.desktop
  cd "${srcdir}/${_pkgname}-${pkgver}"
}

package() {
  install -d "${pkgdir}/opt"
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${pkgdir}/opt/${_pkgname}"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  install -Dm 644 COPYING "${pkgdir}/usr/share/licenses/${_pkgname}/COPYING"
  install -d "${pkgdir}/usr/share/applications"
  install -Dm 644 share/applications/*.desktop "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons"
  cp -a share/icons/hicolor "${pkgdir}/usr/share/icons"
  # Fix bug: http://bugzilla.scilab.org/show_bug.cgi?id=15145
  rm -f -- "${pkgdir}/opt/${_pkgname}/lib/thirdparty/libz.so"*
}
