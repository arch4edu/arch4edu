# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=randomForest
_pkgver=4.7-1.1
pkgname=r-${_pkgname,,}
pkgver=4.7.1.1
pkgrel=3
pkgdesc="Breiman and Cutler's Random Forests for Classification and Regression"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
  r-rcolorbrewer
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f59ea87534480edbcd6baf53d7ec57e8c69f4532c2d2528eacfd48924efa2cd6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
