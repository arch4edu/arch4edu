# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Bayesrel
_pkgver=0.7.4.4
pkgname=r-${_pkgname,,}
pkgver=0.7.4.4
pkgrel=1
pkgdesc='Bayesian Reliability Estimation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-coda
  r-laplacesdemon
  r-lavaan
  r-progress
  r-rcpp
  r-rcpparmadillo
  r-rdpack
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1758963092b28e579f33528120055721022d0b88731620d2014eb8448caab344')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
