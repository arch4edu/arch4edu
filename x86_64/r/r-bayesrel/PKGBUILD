# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Bayesrel
_pkgver=0.7.8
pkgname=r-${_pkgname,,}
pkgver=0.7.8
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
sha256sums=('133a8a3b03cf817a7838ee19297f1335447fc3f7166162c1cf57af208f7d2837')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
