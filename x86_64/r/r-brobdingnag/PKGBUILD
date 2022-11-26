# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Brobdingnag
_pkgver=1.2-9
pkgname=r-${_pkgname,,}
pkgver=1.2.9
pkgrel=3
pkgdesc='Very Large Numbers in R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-cubature
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f9012d250bc2a0f47815d6a7c06df2d4ddf3d8bab2d3b75e8cdefd964d20e91e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
