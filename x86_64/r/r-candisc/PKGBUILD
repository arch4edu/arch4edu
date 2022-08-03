# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=candisc
_pkgver=0.8-6
pkgname=r-${_pkgname,,}
pkgver=0.8.6
pkgrel=4
pkgdesc='Visualizing Generalized Canonical Discriminant and Canonical Correlation Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-car
  r-heplots
)
optdepends=(
  r-corrplot
  r-knitr
  r-mass
  r-rgl
  r-rmarkdown
  r-rpart
  r-rpart.plot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9645a3c0f8a0f7ee1e0c4de6cac4d3432177e6d3975fa538cdb060f5e480709d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
