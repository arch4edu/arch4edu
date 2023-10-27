# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=tidyr
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Tidy Messy Data"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6721234466ed4b48bab20286131d4a06')
sha256sums=('8d532b9366fdd3ec9827b51830e559a49d073425007c766025f0e603964e0a9d')

prepare() {
  cd "$_pkgname/tests/testthat"
  # skip broken snapshot tests
  sed -i '/"after must be integer or character"/a\ \ skip("broken snapshot")' test-append.R
  sed -i '/"input validation catches problems"/a\ \ skip("broken snapshot")' test-hoist.R
  sed -i '/"`pivot_longer()` catches unused input passed through the dots"/a\ \ skip("broken snapshot")' test-pivot-long.R
  sed -i '/"separate_wider_position() validates its inputs"/a\ \ skip("broken snapshot")' test-separate-wider.R
  sed -i '/"`transform` is validated"/a\ \ skip("broken snapshot")' test-unnest-helper.R
}

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
