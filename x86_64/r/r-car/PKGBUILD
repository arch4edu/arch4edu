# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Francois Garillot <francois[@]garillot.net>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=car
_pkgver=3.1-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Companion to Applied Regression"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-abind
  r-cardata
  r-formula
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
  r-ordinal
  r-plotrix
  r-rgl
  r-rio
  r-sandwich
  r-sparsem
  r-survey
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bcc349a3c28cc57f431bcdcec31df241')
b2sums=('a6436041f693acbf9df765a13d0b8ab5790e637330b83cf2cb0600b2f8af9f6b55a899956599e10f8a009537f343e920c04bb303c0e971ca6a5f11214ae5f237')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
