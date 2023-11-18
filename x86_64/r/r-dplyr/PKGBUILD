# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=dplyr
_pkgver=1.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Grammar of Data Manipulation"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-cli
  r-generics
  r-glue
  r-lifecycle
  r-magrittr
  r-pillar
  r-r6
  r-rlang
  r-tibble
  r-tidyselect
  r-vctrs
)
checkdepends=(
  r-lobstr
  r-purrr
  r-rsqlite
  r-stringi
  r-testthat
)
optdepends=(
  r-bench
  r-broom
  r-callr
  r-covr
  r-dbi
  r-dbplyr
  r-ggplot2
  r-knitr
  r-lahman
  r-lobstr
  r-microbenchmark
  r-nycflights13
  r-purrr
  r-rmarkdown
  r-rmysql
  r-rpostgresql
  r-rsqlite
  r-stringi
  r-testthat
  r-tidyr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('29bdf98592722336f0d07484baf2a959')
sha256sums=('cf730414d5d4ab387b4e9890a4b1df9d17a3903488e8da8df1cf2e11e44558cb')

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
