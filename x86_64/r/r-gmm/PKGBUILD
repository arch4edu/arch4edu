# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmm
_pkgver=1.9-1
pkgname=r-${_pkgname,,}
pkgver=1.9.1
pkgrel=1
pkgdesc='Generalized Method of Moments and Generalized Empirical Likelihood'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-sandwich
)
optdepends=(
  r-car
  r-knitr
  r-mass
  r-mvtnorm
  r-stabledist
  r-timedate
  r-timeseries
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9290674d09403f401718dd9c2131a425dba5727b9dcd6698d2f68a9f5ab83c1f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
