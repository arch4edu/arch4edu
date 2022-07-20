# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=qvcalc
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=1.0.2
pkgrel=4
pkgdesc='Quasi Variances for Factor Effects in Statistical Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
  r-psychotools
  r-relimp
  r-survival
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('90cdacc5d1bd429ef7b1ba91f77b5bebee3e4f7f1506b8dcf2a3ac89cefe562d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
