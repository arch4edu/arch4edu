# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Lydgate <archlinux@vo.racio.us>

_pkgname=DBI
_pkgver=1.3.0
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
  r-callr
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
  r-otel
  r-otelsdk
  r-rmariadb
  r-rmarkdown
  r-rprojroot
  r-rsqlite
  r-testthat
  r-vctrs
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ce5e3153cc7395a2aac452db1099d003')
b2sums=('7dab9b801ef28a8a24c3c59823812f9061037604136d796d0920b5f479a871ca1b46f5c716e8514c10352d9cea5500ad08bc4b194f89807af19bc24f476fbadc')

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
