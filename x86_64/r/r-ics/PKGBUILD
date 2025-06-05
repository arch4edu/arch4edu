# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ICS
_pkgver=1.4-2
pkgname=r-${_pkgname,,}
pkgver=1.4.2
pkgrel=1
pkgdesc='Tools for Exploring Multivariate Data via ICS/ICA'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mvtnorm
  r-survey
)
optdepends=(
  r-icsnp
  r-icsoutlier
  r-mass
  r-pixmap
  r-robustbase
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0233531f88dfb641e21f81458986b22477fca2a950be0e0541babc7d9a92db4f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
