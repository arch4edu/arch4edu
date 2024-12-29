# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=emmeans
_pkgver=1.10.6
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fbab0e2c76491fc9208bb3f6b03e5266')
b2sums=('dc164241acd488a7f6eba801f65e851b4222d38a3fdef0e5ae592fb92d7bd54bc8c13dd92ec83ae91707b113e2377177b30ba63b37f5a5bd286647b02e5b519f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
