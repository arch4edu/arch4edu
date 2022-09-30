# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=psych
_pkgver=2.2.9
pkgname=r-${_pkgname,,}
pkgver=2.2.9
pkgrel=1
pkgdesc='Procedures for Psychological, Psychometric, and Personality Research'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mnormt
)
optdepends=(
  r-gparotation
  r-graph
  r-knitr
  r-lavaan
  r-lme4
  r-psychtools
  r-rcsdp
  r-rgraphviz
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4cd518bff387fef95067696b0a0b323310e6f4a063c3d242f2a50bcb17675571')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
