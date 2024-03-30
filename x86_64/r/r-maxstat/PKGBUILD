# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=maxstat
_pkgver=0.7-25
pkgname=r-${_pkgname,,}
pkgver=0.7.25
pkgrel=4
pkgdesc='Maximally Selected Rank Statistics'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-exactranktests
  r-mvtnorm
)
optdepends=(
  r-survival
  r-th.data
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6fc13b8d83797e10fc148183eb440a30584442fdf73628652c606ede790e9f84')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
