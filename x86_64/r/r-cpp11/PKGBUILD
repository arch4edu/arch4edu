# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=cpp11
_pkgver=0.4.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A C++11 Interface for R's C Interface"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r
)
checkdepends=(
  r-decor
  r-knitr
  r-mockery
  r-progress
  r-testthat
)
optdepends=(
  r-bench
  r-brio
  r-callr
  r-cli
  r-covr
  r-decor
  r-desc
  r-ggplot2
  r-glue
  r-knitr
  r-lobstr
  r-mockery
  r-progress
  r-rcpp
  r-rmarkdown
  r-scales
  r-testthat
  r-tibble
  r-vctrs
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('786e1fdd894c982290d4ae401123fe59')
sha256sums=('d1c56954671d3398078ad52aaa4efce0864e8166465c8c5e5e9a1e40599055b3')

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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
