# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=covr
_pkgver=4.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Test Coverage for Packages"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-curl
  r-digest
  r-httr2
  r-jsonlite
  r-rex
  r-rlang
  r-sys
  r-withr
  r-yaml
)
checkdepends=(
  r-box
  r-dt
  r-htmltools
  r-httpuv
  r-memoise
  r-rstudioapi
  r-s7
  r-testthat
  r-xml2
)
optdepends=(
  r-box
  r-callr
  r-covr
  r-htmltools
  r-knitr
  r-memoise
  r-pkgbuild
  r-pkgload
  r-r6
  r-rmarkdown
  r-rstudioapi
  r-s7
  r-shiny
  r-shinytest2
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        )
md5sums=('1ec88f503a5f9e8cf9f42dc45b313fec')
b2sums=('4d3ed7d2869275da92e565c013597993851798df5dc58082d49ea9cf060ac9c68656c73d50faae5a3abdcc9a089e8e105f4187c7a9a3337e19463618e75a0fa7')

# prepare() {
#   # skip failing test
#   patch -Np1 -i fix-tests.patch
# }

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
