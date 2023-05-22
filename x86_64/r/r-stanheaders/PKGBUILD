# system requirements: pandoc
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=StanHeaders
_pkgver=2.26.25
pkgname=r-${_pkgname,,}
pkgver=2.26.25
pkgrel=3
pkgdesc='C++ Header Files for Stan'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
  r-rcppeigen
  r-rcppparallel
)
optdepends=(
  r-bh
  r-knitr
  r-matrix
  r-methods
  r-rcpp
  r-rmarkdown
  r-rstan
  r-withr
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('93bc2d70b26b3652e93a44fcb25c91cc86cd6ac756e6d82b21e1a8d75338baf5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
