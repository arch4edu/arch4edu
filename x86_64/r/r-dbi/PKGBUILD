# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Lydgate <archlinux@vo.racio.us>

_pkgname=DBI
_pkgver=1.2.3
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
md5sums=('062e1bf5ed04772ecb1623c076c2128c')
b2sums=('620906bd0f6b5cdf4f5926bb0cee80480456e907f071e03142a252156339e3e24b3d801cb34ef4e67a5c89992e860fa354010b4975fcd88657110169f43c0aa7')

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
