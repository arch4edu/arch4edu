# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=arm
_pkgver=1.15-3
pkgname=r-${_pkgname,,}
pkgver=1.15.3
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
sha256sums=('94478b0593d751f6c0b2336ed66fee216c7573442a776e5a1eb398a91a50466c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
