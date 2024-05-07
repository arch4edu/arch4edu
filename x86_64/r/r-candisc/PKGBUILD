# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=candisc
_pkgver=0.9.0
pkgname=r-${_pkgname,,}
pkgver=0.9.0
pkgrel=1
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
sha256sums=('a488a51a2931c18d4541a67539892646b67d9d4d286995660e0d2c087a858572')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
