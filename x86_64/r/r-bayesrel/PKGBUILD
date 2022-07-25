# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Bayesrel
_pkgver=0.7.4.2
pkgname=r-${_pkgname,,}
pkgver=0.7.4.2
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
sha256sums=('280c458e02de9d0960d3ff2476f60955c989c8e2ecd1d883f8b97e3f7f7579a2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
