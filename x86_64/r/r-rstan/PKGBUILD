# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=rstan
_pkgver=2.26.23
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="R Interface to Stan"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  pandoc
  r-ggplot2
  r-gridextra
  r-inline
  r-loo
  r-pkgbuild
  r-quickjsr
  r-rcpp
  r-rcppparallel
  r-stanheaders
)
makedepends=(
  r-bh
  r-rcppeigen
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-bayesplot
  r-coda
  r-knitr
  r-rmarkdown
  r-rstanarm
  r-rstantools
  r-rstudioapi
  r-shinystan
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2e01ed18b705fb0fbd0b90e1577f08dc')
sha256sums=('91fddeb9460755e02b7fbc7caa964df8d0d77417528ae96ce3e2f6d56fe60d22')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
