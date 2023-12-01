# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=haven
_pkgver=2.5.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Import and Export 'SPSS', 'Stata' and 'SAS' Files"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-cli
  r-forcats
  r-hms
  r-lifecycle
  r-readr
  r-rlang
  r-tibble
  r-tidyselect
  r-vctrs
  readstat
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-crayon
  r-fs
  r-knitr
  r-pillar
  r-rmarkdown
  r-testthat
  r-utf8
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-readstat.patch")
md5sums=('ef0337da48b61ae98b03413e02177822'
         '73da7cc2ff7f7c1a5d4ffbaa45e359df')
sha256sums=('9e1531bb37aa474abd91db5e0ed9e3a355c03faa65f4e653b3ea68b7c61ea835'
            '8986ddaefd714bd4d2a42364863437116b14f38275196720d88d247794b94bf8')

prepare() {
  # build with system readstat
  patch -Np1 -i system-readstat.patch
}

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
