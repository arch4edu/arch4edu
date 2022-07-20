# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Rtsne
_pkgver=0.16
pkgname=r-${_pkgname,,}
pkgver=0.16
pkgrel=5
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
sha256sums=('52a05adc826c28212e97d11c54eba3fec45d14eb52039c0f47f62a8e338ffbd5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
