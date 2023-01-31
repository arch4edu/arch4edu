# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=TruncatedNormal
_pkgver=2.2.2
pkgname=r-${_pkgname,,}
pkgver=2.2.2
pkgrel=1
pkgdesc='Truncated Multivariate Normal and Student Distributions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-alabama
  r-nleqslv
  r-randtoolbox
  r-rcpp
  r-rcpparmadillo
)
optdepends=(
  r-cardata
  r-knitr
  r-mvtnorm
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('aef567e8962a64d1afbdfd98ab8f385f32966c3c42acb54ee20f02dceab18e15')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
