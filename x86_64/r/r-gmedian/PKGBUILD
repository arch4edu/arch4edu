# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Gmedian
_pkgver=1.2.7
pkgname=r-${_pkgname,,}
pkgver=1.2.7
pkgrel=1
pkgdesc='Geometric Median, k-Medians Clustering and Robust Median PCA'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-rcpparmadillo
  r-robustbase
  r-rspectra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5378666a91de7a7bed078626869362ed5f0d0587dd5e78b1ec3d54e249b92e55')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
