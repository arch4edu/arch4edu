# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=DBI
_pkgver=1.1.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="R Database Interface"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(LGPL)
depends=(
  r
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-blob
  r-covr
  r-dbitest
  r-dbplyr
  r-downlit
  r-dplyr
  r-glue
  r-hms
  r-knitr
  r-magrittr
  r-rmariadb
  r-rmarkdown
  r-rprojroot
  r-rsqlite
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('39053945cef7f76c45c8bc6f5733033f')
sha256sums=('38bb33753da5bddb78893a5228a5d269dae3bf16f21dc5d9853ac9c24d31428d')

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
