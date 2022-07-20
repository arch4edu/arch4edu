# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSpectra
_pkgver=0.16-1
pkgname=r-${_pkgname,,}
pkgver=0.16.1
pkgrel=1
pkgdesc='Solvers for Large-Scale Eigenvalue and SVD Problems'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MPL2')
depends=(
  r
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-knitr
  r-prettydoc
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('cba5d3403d6a7d0e27abf6279fbfea6e0d0fe36b28c688bbadb8eafb3841329a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
