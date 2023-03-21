# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=truncnorm
_pkgver=1.0-9
pkgname=r-${_pkgname,,}
pkgver=1.0.9
pkgrel=1
pkgdesc='Truncated Normal Distribution'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5156acc4d63243bf95326d6285b0ba3cdf710697d67c233a12ae56f3d87ec708')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
