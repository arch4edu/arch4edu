# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=emmeans
_pkgver=2.0.1
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
md5sums=('5c7fbaf108f412d10402bcb47bc80492')
b2sums=('b9d4dde96633c65ac7e6d3580cbbbbdc54ba3aa3f06178fefe67c4cd6a61624d9399c048fcac2db1cf78c666c335243e3d97b55ef74df4417ec9d9f3cb694c22')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
