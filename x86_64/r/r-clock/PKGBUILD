# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clock
_pkgver=0.7.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Date-Time Types and Tools"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-lifecycle
  r-rlang
  r-tzdb
  r-vctrs
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-slider
  r-testthat
)
optdepends=(
  r-covr
  r-knitr
  r-magrittr
  r-pillar
  r-rmarkdown
  r-slider
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1d18204eb746247d7dde0cc1353300b8')
b2sums=('0488c741f9fe7780bc086ab37b09e85e923abe4b6bf95d7de595d078b694cf9d2049c7ef32f107f8e55452ac1c6cf9970d14cfbe162fc4b9fcc5ac5cb3f5701e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
