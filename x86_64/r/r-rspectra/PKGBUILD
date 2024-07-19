# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RSpectra
_pkgver=0.16-2
pkgname=r-${_pkgname,,}
pkgver=0.16.2
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
sha256sums=('a2f149d79519fee79dabe1b174dfb847a916045315d5927a93cc6b005522aa7e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
