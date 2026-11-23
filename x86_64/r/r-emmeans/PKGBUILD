# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=emmeans
_pkgver=2.0.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Estimated Marginal Means, aka Least-Squares Means"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-estimability
  r-mvtnorm
  r-numderiv
  r-rlang
)
optdepends=(
  r-bayesplot
  r-bayestestr
  r-biglm
  r-brms
  r-car
  r-coda
  r-compositions
  r-ggplot2
  r-knitr
  r-lme4
  r-lmertest
  r-logspline
  r-mediation
  r-multcomp
  r-multcompview
  r-mumin
  r-ordinal
  r-pbkrtest
  r-rmarkdown
  r-rsm
  r-sandwich
  r-scales
  r-testthat
  r-tibble
  r-xtable
  r-robmixglm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4d3747a7d485e4257283af04aab82322')
b2sums=('0db045beebcefff9eb6e3333d3e5f1c71bfdb89fc69a73340331e136c554c69c6a307503a3de71ac0e7ea072f6695b4d206763fe4efe401c0144c7a21eac6f2b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
