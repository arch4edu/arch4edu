# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=cubature
_pkgver=2.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Adaptive Multivariate Integration over Hypercubes"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-rcpp
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-benchr
  r-knitr
  r-mvtnorm
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2ba4be5bef4581b51748b04105ec4c8b')
b2sums=('bd8e563e5613733ef170daf9ece2c8b4231bbefd0776c3ce74baaa8502e35ee6681b4bd924b4dc141df829f75d85dc4267fe8eb0e8b4982d41b9fa4ef18b0a6f')

build() {
  mkdir build
  # parallel build results in undefined behavior
  MAKEFLAGS="-j1" R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
