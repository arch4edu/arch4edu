# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=scilab-beta-bin
_pkgver=6.0.0-beta-2
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A scientific software package for numerical computations."
arch=("x86_64" "i686")
license=("BSD" "custom:CeCILL")
conflicts=('scilab' 'scilab-bin' 'scilab-git')
url="https://www.scilab.org"

source=("scilab.sh")
md5sums=('32bba7f8af6ead4bdacfe40a67d4b30e')
md5sums_x86_64=('c45735f9324c5f54c31630f512533f7e')
md5sums_i686=('7cbdb9323426971c1e0fe7d75e5edbbe')

source_x86_64=("http://www.scilab.org/download/${_pkgver}/scilab-${_pkgver}.bin.linux-x86_64.tar.gz")

source_i686=("http://www.scilab.org/download/${_pkgver}/scilab-${_pkgver}.bin.linux-i686.tar.gz")

# Standalone package
depends=()

package() {
  cd "${srcdir}"

  install -d "${pkgdir}/opt"
  cp -r "${srcdir}/scilab-${_pkgver}" "${pkgdir}/opt/scilab"

  install -Dm 644 "${srcdir}/scilab-${_pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"

  install -d "${pkgdir}/usr/share/applications"
  install -Dm 644 "${srcdir}/scilab-${_pkgver}/share/applications/scilab.desktop" "${pkgdir}/usr/share/applications/scilab.desktop"

  install -d "${pkgdir}/usr/share/icons"
  cp -r "${srcdir}/scilab-${_pkgver}/share/icons/hicolor" "${pkgdir}/usr/share/icons/"

  install -Dm 755 scilab.sh "${pkgdir}/usr/bin/scilab"
}
