# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mi
_pkgver=1.2
pkgname=r-${_pkgname,,}
pkgver=1.2
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
sha256sums=('06d209b4e031ee0431421041f698804006f86eefff10779bc246e3fd22dc6d8c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
