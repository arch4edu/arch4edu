# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Bayesrel
_pkgver=0.8.0
pkgname=r-${_pkgname,,}
pkgver=0.8.0
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
  r-rcpp
  r-rcpparmadillo
  r-rdpack
  r-psych
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e87e12bea90c636d0308715d5097c364564f30cb938812d5700d6c193a2bd03d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
