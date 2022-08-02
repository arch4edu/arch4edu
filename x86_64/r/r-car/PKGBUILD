# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=car
_pkgver=3.1-0
pkgname=r-${_pkgname,,}
pkgver=3.1.0
pkgrel=1
pkgdesc='Companion to Applied Regression'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-abind
  r-cardata
  r-lme4
  r-maptools
  r-pbkrtest
  r-quantreg
)
optdepends=(
  r-alr4
  r-boot
  r-coxme
  r-effects
  r-knitr
  r-leaps
  r-lmtest
  r-matrix
  r-matrixmodels
  r-rgl
  r-rio
  r-sandwich
  r-sparsem
  r-survey
  r-survival
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bd52b4eaea46ce828fccd93445301d06ebd265e2ffff796064875a8c0f0aea21')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
