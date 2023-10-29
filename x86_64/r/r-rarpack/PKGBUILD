# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rARPACK
_pkgver=0.11-0
pkgname=r-${_pkgname,,}
pkgver=0.11.0
pkgrel=4
pkgdesc='Solvers for Large Scale Eigenvalue and SVD Problems'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
  r-rspectra
)
optdepends=(
  r-matrix
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c33401e2e31d272d485ce2ed22e7fe43ac641fd7c0a45a9b848d3ad60df1028a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
