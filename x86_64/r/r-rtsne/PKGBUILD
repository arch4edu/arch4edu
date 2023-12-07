# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Rtsne
_pkgver=0.17
pkgname=r-${_pkgname,,}
pkgver=0.17
pkgrel=1
pkgdesc='T-Distributed Stochastic Neighbor Embedding using a Barnes-Hut Implementation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('custom')
depends=(
  r
  r-rcpp
)
optdepends=(
  r-irlba
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3aae6814d6c6d406785145f07374135652f2b26a58690dfd4bfbc8365dc5590b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
