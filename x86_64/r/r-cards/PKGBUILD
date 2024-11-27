# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=cards
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Analysis Results Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
depends=(
  r-cli
  r-dplyr
  r-glue
  r-rlang
  r-tidyr
  r-tidyselect
)
checkdepends=(
  r-hms
  r-testthat
)
optdepends=(
  r-spelling
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cef71180716bfa6b54d633564a1b9d8e')
b2sums=('ca2a4419064f471276151a0e6feb4c758c27b959e3a0ab82ae5703df3ba6d839c5f9936fb2b999c0d13234142ad869dc63dc6f2b631cdfb8615cf8b582c6f7cb')

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
