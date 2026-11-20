# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=arm
_pkgver=1.15-4
pkgname=r-${_pkgname,,}
pkgver=1.15.4
pkgrel=1
pkgdesc='Data Analysis Using Regression and Multilevel/Hierarchical Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-abind
  r-coda
  r-lme4
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c6e7bc57ae45f9450088933c1bd4b00d7c0daaf356433522e3f256ffe7a3a0cc')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
