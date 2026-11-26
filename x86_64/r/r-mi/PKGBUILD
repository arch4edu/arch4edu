# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mi
_pkgver=1.3.3
pkgname=r-${_pkgname,,}
pkgver=1.3.3
pkgrel=1
pkgdesc='Missing Data Imputation and Model Checking'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-arm
)
optdepends=(
  r-betareg
  r-foreign
  r-knitr
  r-lattice
  r-mass
  r-nnet
  r-parallel
  r-sn
  r-survival
  r-truncnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2c97435c4101cae9a866523427bb9a97afb4e9027230f3bd22f7866444d8f78e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
