# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Lydgate <archlinux@vo.racio.us>

_pkgname=DBI
_pkgver=1.2.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="R Database Interface"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-arrow
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
  r-nanoarrow
  r-rmariadb
  r-rmarkdown
  r-rprojroot
  r-rsqlite
  r-testthat
  r-vctrs
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f7e3698666cec735a4e0da7e18dc025c')
b2sums=('4e222f499b5262de4d24fd0a8cb31d03382c964ed6089da342454fce13684799ab960f11ab0d4571e09524ba52f8ed19641d43bd798a0d56d5d92380a5e70211')

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
}
