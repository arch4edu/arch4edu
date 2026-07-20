# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=webshot2
_pkgver=0.1.2
pkgname=r-webshot2
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Take Screenshots of Web Pages"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT + file LICENSE)
depends=(r r-callr r-chromote r-later r-magrittr r-promises)
makedepends=(gcc-fortran)
optdepends=(r-httpuv r-rmarkdown r-shiny)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha256sums=('27aa449ef9174c0563c5905800bc85eb1106c3470a3075e3d8040e4eda782e94')
