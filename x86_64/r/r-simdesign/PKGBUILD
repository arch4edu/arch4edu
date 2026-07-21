# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=SimDesign
_pkgver=2.25
pkgname=r-simdesign
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Structure for Organizing Monte Carlo Simulation Designs"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-beepr r-clipr r-dplyr r-e1071 r-future r-future.apply r-mirai r-parallelly r-pbapply r-progressr r-qs2 r-r.utils r-sessioninfo r-testthat)
makedepends=(gcc-fortran)
optdepends=(r-cli r-copula r-extradistr r-frf2 r-future.batchtools r-ggplot2 r-httr r-job r-knitr r-purrr r-renv r-rmarkdown r-rpushbullet r-shiny r-snow r-tidyr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('5d03e5e4e14f7f2576d79882ffbb487adfcf823f9e1f690dc7942b192246086f')
