# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=dplyr
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
  r-broom
  r-covr
  r-dbi
  r-dbplyr
  r-ggplot2
  r-knitr
  r-lahman
  r-lobstr
  r-nycflights13
  r-purrr
  r-rmarkdown
  r-rsqlite
  r-stringi
  r-testthat
  r-tidyr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('1c6ba2499c7a08d081bdb530423ab22c'
         '386fe9fd45e30f6833f4c4f86b86b2ea')
b2sums=('79a37ce9cc46162f530602770b56a81091fef9a3180c72a57e92669b6a9beea86f03754a5a14615ef9741f7b88babf12ef6c7a96b4239cc631c4cbd1d2d62aac'
        '304013a86b786a05f53a57c124c73af4941c3a91ee9d2ef8facfb4d15d6b864c2b75fc3ace66c532dfdfd6c81fe01bb22bd2e3ecbf65b31c0992cc34ec507647')

_prepare() {
  # fix test snapshots
  patch -Np1 -i fix-tests.patch
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
