# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=pROC
_pkgver=1.19.0.1
pkgname=r-${_pkgname,,}
pkgver=1.19.0.1
pkgrel=1
pkgdesc='Display and Analyze ROC Curves'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-plyr
  r-rcpp
)
optdepends=(
  r-doparallel
  r-ggplot2
  r-logcondens
  r-mass
  r-microbenchmark
  r-rlang
  r-tcltk
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f161ed071a3c45192f0faf4ab37237f12bed9334e954e5e041ba98078c70e619')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
