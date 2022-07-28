# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ROCR
_pkgver=1.0-11
pkgname=r-${_pkgname,,}
pkgver=1.0.11
pkgrel=4
pkgdesc='Visualizing the Performance of Scoring Classifiers'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gplots
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('57385a773220a3aaef5b221a68b2d9c2a94794d4f9e9fc3c1eb9521767debb2a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
