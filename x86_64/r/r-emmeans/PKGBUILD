# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=emmeans
_pkgver=2.0.2
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
md5sums=('26de266c7a7079a5dd07634d4dca8479')
b2sums=('8d841ff89baac95aa31c7bc37a730675bff446395f499e82fd5d76f86c753df6bec60d9304854b4d4cc9779ee52ac716c76db0e43fe7877b4eca10615e4b17e1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
