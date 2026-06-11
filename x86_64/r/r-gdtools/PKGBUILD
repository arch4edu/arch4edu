# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: portaloffreedom

_pkgname=gdtools
_pkgver=0.5.1
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
md5sums=('eb8b6f792f150c2cbccaac67f7b12fda')
b2sums=('56ca35be55b9b9ba82299dbd75e730e50a21d5996b913cd19f95b70f88ec789121f76a386806ff3f5d9b21b21f38d910eebb706dc42aded4e2724ce926483feb')

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
