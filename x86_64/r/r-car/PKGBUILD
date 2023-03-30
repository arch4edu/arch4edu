# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=car
_pkgver=3.1-2
pkgname=r-${_pkgname,,}
pkgver=3.1.2
pkgrel=1
pkgdesc='Companion to Applied Regression'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-abind
  r-cardata
  r-lme4
  r-pbkrtest
  r-quantreg
  r-scales
)
optdepends=(
  r-alr4
  r-boot
  r-coxme
  r-effects
  r-knitr
  r-leaps
  r-lmtest
  r-matrix
  r-matrixmodels
  r-mvtnorm
  r-rgl
  r-rio
  r-sandwich
  r-sparsem
  r-survey
  r-survival
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('89263491977ac8e9406b2f4b1638bf06c7ddd1b0e0e3ecda4be61420474674c8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
