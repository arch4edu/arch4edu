# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=geepack
_pkgver=1.3.12
pkgname=r-${_pkgname,,}
pkgver=1.3.12
pkgrel=1
pkgdesc='Generalized Estimating Equation Package'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-broom
  r-magrittr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e01be9555155ecd6d4dee2e566066c2a6e0953d0e3a58bb31fa5c07f3834054d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
