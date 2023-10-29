# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Francois Garillot <francois[@]garillot.net>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=car
_pkgver=3.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Companion to Applied Regression"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-abind
  r-cardata
  r-lme4
  r-pbkrtest
  r-quantreg
  r-scales
)
optdepends=(
  r-alr4
  r-coxme
  r-effects
  r-knitr
  r-leaps
  r-lmtest
  r-matrixmodels
  r-mvtnorm
  r-rgl
  r-rio
  r-sandwich
  r-sparsem
  r-survey
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f8be85a665aa367951aacf80d89eb5e9')
sha256sums=('89263491977ac8e9406b2f4b1638bf06c7ddd1b0e0e3ecda4be61420474674c8')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
