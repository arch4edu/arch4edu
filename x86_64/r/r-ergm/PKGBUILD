# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=ergm
_pkgver=4.12.0
pkgname=r-ergm
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fit, Simulate and Diagnose Exponential-Family Models for Networks"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL-3)
depends=(r r-cli r-coda r-knitr r-lpsolveapi r-magrittr r-memoise r-network r-purrr r-rdpack r-rlang r-rle r-robustbase r-statnet.common r-stringr r-tibble r-trust)
makedepends=(gcc-fortran)
optdepends=(r-covr r-ergm.count r-latticeextra r-networklite r-rglpk r-rmarkdown r-slam r-sna r-testthat r-withr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('eb4aef2dd6fc0fe816f4e25962b13c26eaf6c71bc4c96df43fa090a5f9c363b5')
