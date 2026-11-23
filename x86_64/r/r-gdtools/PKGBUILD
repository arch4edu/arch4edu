# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: portaloffreedom

_pkgname=gdtools
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Font Metrics and Font Management Utilities for R Graphics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  cairo
  freetype2
  r-fontquiver
  r-htmltools
  r-rcpp
  r-systemfonts
)
checkdepends=(
  r-gfonts
  r-testthat
)
optdepends=(
  r-curl
  r-gfonts
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a13f49fbca3517c2a82f5f9a7f0b18db')
b2sums=('841fbe5651165f343bd84b0aec57825f3942741894ab9bbeda904a09d8f501e04d645a12d73debbc3e80ff6d6b64c76212a6b339af27349b5275cbd6dcc40d10')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

# check() {
#   cd "$_pkgname/tests"
#   R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
# }

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
