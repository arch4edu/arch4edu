# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=candisc
_pkgver=1.1.1
pkgname=r-${_pkgname,,}
pkgver=1.1.1
pkgrel=1
pkgdesc='Visualizing Generalized Canonical Discriminant and Canonical Correlation Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-car
  r-heplots
  r-insight
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
sha256sums=('08de55c084e570fd8db665476f048f914866f8f27714f1bc3a33aacd6b998e0b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
