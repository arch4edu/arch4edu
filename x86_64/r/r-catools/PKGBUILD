# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Sauliusl <luksaulius at gmail>

_pkgname=caTools
_pkgver=1.18.2
pkgname=r-${_pkgname,,}
pkgver=1.18.2
pkgrel=7
pkgdesc='Tools: Moving Window Statistics, GIF, Base64, ROC AUC, etc'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bitops
)
optdepends=(
  r-mass
  r-rpart
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('75d61115afec754b053ed1732cc034f2aeb27b13e6e1932aa0f26bf590cf0293')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
