# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=flexmix
_pkgver=2.3-18
pkgname=r-${_pkgname,,}
pkgver=2.3.18
pkgrel=1
pkgdesc='Flexible Mixture Modeling'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-modeltools
)
optdepends=(
  r-actuar
  r-codetools
  r-diptest
  r-ecdat
  r-ellipse
  r-gclus
  r-glmnet
  r-lme4
  r-mass
  r-mgcv
  r-mlbench
  r-multcomp
  r-mvtnorm
  r-suppdists
  r-survival
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('462201ef49088845c83083e4ed6725cf069aafb12a814041618aaf09ebd69b51')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
