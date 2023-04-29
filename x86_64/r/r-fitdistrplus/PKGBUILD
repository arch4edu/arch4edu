# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fitdistrplus
_pkgver=1.1-11
pkgname=r-${_pkgname,,}
pkgver=1.1.11
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
  r-bookdown
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
sha256sums=('26274f2b710b2417a8bca314d400abf320d4ccf0387ad082743056699501b53d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
