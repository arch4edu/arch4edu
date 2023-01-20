# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=pbkrtest
_pkgver=0.5.2
pkgname=r-${_pkgname,,}
pkgver=0.5.2
pkgrel=1
pkgdesc='Parametric Bootstrap, Kenward-Roger and Satterthwaite Based Methods for Test in Mixed Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-broom
  r-dplyr
  r-knitr
  r-lme4
  r-magrittr
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8e79adf035a0fcf3c82145ad55847497379e009f7be880ba3007ebeb2e69b6e3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
