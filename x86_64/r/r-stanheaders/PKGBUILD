# system requirements: pandoc
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=StanHeaders
_pkgver=2.32.5
pkgname=r-${_pkgname,,}
pkgver=2.32.5
pkgrel=1
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
sha256sums=('54123b1ff403582a1c83a927b887a21da863786cf98d3b9eeed777e1bbd11773')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
