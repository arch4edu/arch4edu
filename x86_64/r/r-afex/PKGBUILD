# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=afex
_pkgver=1.5-1
pkgname=r-${_pkgname,,}
pkgver=1.5.1
pkgrel=1
pkgdesc='Analysis of Factorial Experiments'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-car
  r-lme4
  r-lmertest
  r-pbkrtest
  r-reshape2
)
optdepends=(
  r-brms
  r-cardata
  r-coin
  r-cowplot
  r-dfoptim
  r-dplyr
  r-effects
  r-emmeans
  r-ez
  r-ggbeeswarm
  r-ggplot2
  r-ggpol
  r-ggpubr
  r-ggresidpanel
  r-glmmtmb
  r-grid
  r-jtools
  r-knitr
  r-lattice
  r-latticeextra
  r-mass
  r-matrix
  r-memss
  r-mlmrev
  r-multcomp
  r-nlme
  r-nloptr
  r-optimx
  r-parallel
  r-performance
  r-plyr
  r-psychtools
  r-r.rsp
  r-rmarkdown
  r-rstanarm
  r-see
  r-statmod
  r-testthat
  r-tidyr
  r-vdiffr
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('68c5bb370579e288c4e11603a84aa637d2c44995faee10ebc2b42ebd86c03dbb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
