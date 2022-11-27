# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=lme4
_pkgver=1.1-31
pkgname=r-${_pkgname,,}
pkgver=1.1.31
pkgrel=3
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
  r-merderiv
  r-mgcv
  r-mlmrev
  r-numderiv
  r-optimx
  r-pbkrtest
  r-rmarkdown
  r-rr2
  r-semeff
  r-statmod
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5affd1e33d3fece5ec0a6c7663eb12328e64147f8aa92675ce6453c4fe72edfd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
