# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Lydgate <archlinux@vo.racio.us>

_pkgname=DBI
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="R Database Interface"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(LGPL)
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
md5sums=('5c74f3d0cbf627e67eb4d0557369411b')
b2sums=('5c68048b9aa25161dda417128e0444184e3be249373c38277e4de40a4165b49e9020db603e1682cbacbb06d63e839afeafdfc1933915d3c0218fbd4fea28430b')

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
