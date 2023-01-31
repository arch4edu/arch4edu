# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=logistf
_pkgver=1.24.1
pkgname=r-${_pkgname,,}
pkgver=1.24.1
pkgrel=3
pkgdesc="Firth's Bias-Reduced Logistic Regression"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-formula.tools
  r-mice
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e7e0d9054cf7f3221ba363afa0fdf1c8bb65b8841700ec0010fa4886be26a661')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
