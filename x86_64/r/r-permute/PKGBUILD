# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=permute
_pkgver=0.9-7
pkgname=r-${_pkgname,,}
pkgver=0.9.7
pkgrel=10
pkgdesc='Functions for Generating Restricted Permutations of Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-bookdown
  r-knitr
  r-parallel
  r-rmarkdown
  r-sessioninfo
  r-testthat
  r-vegan
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('eff88ffb579aaeb994e9f8609b776b2d9d9d56bc2879ddf180e3a2ad19f48dc0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
