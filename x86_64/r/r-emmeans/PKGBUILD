# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=emmeans
_pkgver=1.8.0
pkgname=r-${_pkgname,,}
pkgver=1.8.0
pkgrel=1
pkgdesc='Estimated Marginal Means, aka Least-Squares Means'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-estimability
  r-mvtnorm
  r-numderiv
  r-xtable
)
optdepends=(
  r-bayesplot
  r-bayestestr
  r-biglm
  r-brms
  r-car
  r-carbayes
  r-coda
  r-coxme
  r-gee
  r-geepack
  r-ggplot2
  r-knitr
  r-lattice
  r-lme4
  r-lmertest
  r-logspline
  r-mass
  r-mcmcglmm
  r-mcmcpack
  r-mediation
  r-mgcv
  r-mice
  r-multcomp
  r-multcompview
  r-mumin
  r-nlme
  r-nnet
  r-ordinal
  r-pbkrtest
  r-pscl
  r-rmarkdown
  r-rsm
  r-rstanarm
  r-scales
  r-sommer
  r-splines
  r-survival
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('232536939bd0a4b7e8d9f5a191d8e2e7e34a45b2a5dcd591359357ee995cbb75')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
