# Maintainer: Marcel Hasler <mahasler at gmail dot com>

pkgname=scilab-bin
pkgver=5.5.2
pkgrel=1
pkgdesc="A scientific software package for numerical computations."
arch=("x86_64" "i686")
license=("BSD" "custom:CeCILL")
url="https://www.scilab.org"

source=("scilab.sh")
md5sums=("32bba7f8af6ead4bdacfe40a67d4b30e")

source_x86_64=("http://www.scilab.org/download/${pkgver}/scilab-${pkgver}.bin.linux-x86_64.tar.gz")
md5sums_x86_64=("c24553bc2bf9871d71decd99c2d73d78")

source_i686=("http://www.scilab.org/download/${pkgver}/scilab-${pkgver}.bin.linux-i686.tar.gz")
md5sums_i686=("71d794854e85d484b12a8b8c954f03c4")

# Standalone package
depends=()

package() {
  cd "${srcdir}"

  install -d "${pkgdir}/opt"
  cp -r "${srcdir}/scilab-${pkgver}" "${pkgdir}/opt/scilab"

  install -Dm 644 "${srcdir}/scilab-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"

  install -d "${pkgdir}/usr/share/applications"
  install -Dm 644 "${srcdir}/scilab-${pkgver}/share/applications/scilab.desktop" "${pkgdir}/usr/share/applications/scilab.desktop"

  install -d "${pkgdir}/usr/share/icons"
  cp -r "${srcdir}/scilab-${pkgver}/share/icons/hicolor" "${pkgdir}/usr/share/icons/"

  install -Dm 755 scilab.sh "${pkgdir}/usr/bin/scilab"
}
