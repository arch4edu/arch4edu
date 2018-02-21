# Maintainer  : George Eleftheriou <eleftg>
# Contributor : Marcel Hasler <mahasler at gmail dot com>

pkgname=scilab-bin
_pkgname=${pkgname%-bin}
pkgver=6.0.1
pkgrel=1
pkgdesc="A software package for numerical computation, providing a powerful computing environment for engineering and scientific applications."
arch=("x86_64")
license=("BSD" "custom:CeCILL")
url="https://www.scilab.org"
# Standalone package
depends=()
conflicts=('scilab')
options=(!strip)
source=("http://www.scilab.org/download/${pkgver}/scilab-${pkgver}.bin.linux-x86_64.tar.gz")
sha256sums=("ad8c66cf6df3d761c830c52e1dfe2ca0f3cb5ec241e107def79b04663fe59ae9")

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}/share/applications"
  sed -i "s|Exec=scilab-adv-cli|Exec=/opt/scilab/bin/scilab-adv-cli|" scilab-adv-cli.desktop
  sed -i "s|Exec=scilab-cli|Exec=/opt/scilab/bin/scilab-cli|" scilab-cli.desktop
  sed -i "s|Exec=scilab -f|Exec=/opt/scilab/bin/scilab -f %f|" scilab.desktop
  sed -i "s|Terminal=false|Terminal=true|" scilab.desktop
  sed -i "s|Exec=scinotes|Exec=/opt/scilab/bin/scinotes|" scinotes.desktop
  sed -i "s|Exec=xcos|Exec=/opt/scilab/bin/xcos|" xcos.desktop
  sed -i "s|Terminal=false|Terminal=true|" xcos.desktop
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
}
