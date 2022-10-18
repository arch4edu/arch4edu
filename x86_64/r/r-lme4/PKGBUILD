# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=lme4
_pkgver=1.1-30
pkgname=r-${_pkgname,,}
pkgver=1.1.30
pkgrel=4
pkgdesc="Linear Mixed-Effects Models using 'Eigen' and S4"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-minqa
  r-nloptr
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-car
  r-dfoptim
  r-gamm4
  r-ggplot2
  r-hsaur3
  r-knitr
  r-memss
  r-mgcv
  r-mlmrev
  r-numderiv
  r-optimx
  r-pbkrtest
  r-pkpdmodels
  r-rmarkdown
  r-rr2
  r-semeff
  r-statmod
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fdabdfc4b64cff05ae9506a766c948a953eeb6db71761f9401b36d6d9979300f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
