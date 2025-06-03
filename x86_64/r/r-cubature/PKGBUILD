# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=cubature
_pkgver=2.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('fcb2f2dea08d5b71e3b770b901f15349')
b2sums=('f4c4cdf7a8f6f2169c593c2c380e169b888570bd0d9a0dd36bf4906a7b869826fcde557304a19de7464907a1f51238a733a44acbbd5e8122e2d88ae541452f8f')

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
