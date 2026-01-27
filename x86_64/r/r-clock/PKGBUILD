# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clock
_pkgver=0.7.4
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
md5sums=('ebf75c3093bd8f58f6d258dfee7e89ad')
b2sums=('b1aff3b88c5b818583f10a019a14aaba43f459cf8a0afe7e7c7376c486496a37cd365224e985c82bded8cdd771bcaccd4bfd64b65adf19c0f9e34a3c7bf34d89')

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
