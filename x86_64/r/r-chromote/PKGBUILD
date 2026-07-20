# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=chromote
_pkgver=0.5.1
pkgname=r-chromote
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Headless Chrome Web Browser Interface"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT + file LICENSE)
depends=(r r-cli r-curl r-fastmap r-jsonlite r-later r-magrittr r-processx r-promises r-r6 r-rlang r-websocket r-withr r-zip)
makedepends=(gcc-fortran)
optdepends=(r-knitr r-rmarkdown r-showimage r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
sha256sums=('b0caa76507a2dea3c524c84d99ca0ac77eb8b46b60adc02fbc80c67741b354b5')
