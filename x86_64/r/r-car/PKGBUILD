# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=car
_pkgver=3.1-1
pkgname=r-${_pkgname,,}
pkgver=3.1.1
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
  r-maptools
  r-pbkrtest
  r-quantreg
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
  r-rgl
  r-rio
  r-sandwich
  r-sparsem
  r-survey
  r-survival
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8fc55815eed7e46a32b54da9e0bfa4b74a8d082d73d896e3372f2a413b6bd2bc')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
