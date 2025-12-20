# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=tidyr
_pkgver=1.3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tidy Messy Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dplyr
  r-glue
  r-lifecycle
  r-magrittr
  r-purrr
  r-rlang
  r-stringr
  r-tibble
  r-tidyselect
  r-vctrs
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-data.table
  r-testthat
)
optdepends=(
  r-covr
  r-data.table
  r-knitr
  r-readr
  r-repurrrsive
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
)
md5sums=('f8e976221d4ed9092c734cf86abcdba9')
b2sums=('7db5da35771bcbb4affe0517a18d200d15ad78ecb7675eed6f85f6c4cce66289a0c377e9edf8f617eb3bfaa32078e6806aa976caeacbd9b38198e6ee4aabc1f4')


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
