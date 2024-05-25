# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmm
_pkgver=1.8
pkgname=r-${_pkgname,,}
pkgver=1.8
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
sha256sums=('7099fc5c6a9069924392995a726190e8d62f6e55375ef356084b0c73346d85d8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
