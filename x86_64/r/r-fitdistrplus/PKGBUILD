# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fitdistrplus
_pkgver=1.1-8
pkgname=r-${_pkgname,,}
pkgver=1.1.8
pkgrel=3
pkgdesc='Help to Fit of a Parametric Distribution to Non-Censored or Censored Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-actuar
  r-gamlss.dist
  r-generalizedhyperbolic
  r-ggplot2
  r-hmisc
  r-knitr
  r-mc2d
  r-rgenoud
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f3c72310f40773b3839a9506c3cb781d044e09b94f2f38d332bb24e5f9960f5a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
