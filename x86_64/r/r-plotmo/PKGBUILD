# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=plotmo
_pkgver=3.6.3
pkgname=r-${_pkgname,,}
pkgver=3.6.3
pkgrel=1
pkgdesc="Plot a Model's Residuals, Response, and Partial Dependence Plots"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-formula
  r-plotrix
  r-teachingdemos
)
optdepends=(
  r-c50
  r-earth
  r-gbm
  r-glmnet
  r-glmnetutils
  r-mass
  r-mlr
  r-neuralnet
  r-partykit
  r-pre
  r-rpart
  r-rpart.plot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6917cd8185325f1f2998fb14def9e6a8d93f1b708cf70d7c443d3960c9189b7b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
