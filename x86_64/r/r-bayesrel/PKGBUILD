# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Bayesrel
_pkgver=0.7.9
pkgname=r-${_pkgname,,}
pkgver=0.7.9
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
sha256sums=('91e21b0e64d17ddea86fae46647631f5af417265648c66b761b4d0a65bd0b24c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
