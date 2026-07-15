# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=emmeans
_pkgver=2.0.4
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
md5sums=('5ddcca53290680d7f7753ed71892d887')
b2sums=('34c15a7479fb2671c1f8934657cefa36ab21b7e60ac5ea8425be90410d6efcb38427c54910f8ac72a1db14a83c6b5f0b31b8498dda5fdb315c1c2d105c01f431')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
