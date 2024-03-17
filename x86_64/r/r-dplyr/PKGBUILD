# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=dplyr
_pkgver=1.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="A Grammar of Data Manipulation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('29bdf98592722336f0d07484baf2a959'
         '386fe9fd45e30f6833f4c4f86b86b2ea')
b2sums=('3f16d1b818bae28f1cda84244378d9a4a1981cad6ee00ce1f905d5828b8dd4a29d2f4bfe161483300924784c3bdab2cc02a16571042776922dc4bfb845b351da'
        '304013a86b786a05f53a57c124c73af4941c3a91ee9d2ef8facfb4d15d6b864c2b75fc3ace66c532dfdfd6c81fe01bb22bd2e3ecbf65b31c0992cc34ec507647')

prepare() {
  # fix test snapshots
  patch -Np1 -i fix-tests.patch
}

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
