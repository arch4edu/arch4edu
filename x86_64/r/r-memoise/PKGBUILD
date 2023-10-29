# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=memoise
_pkgver=2.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=8
pkgdesc="'Memoisation' of Functions"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-cachem
  r-rlang
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-aws.s3
  r-covr
  r-digest
  r-googleauthr
  r-googlecloudstorager
  r-httr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('89da4ce771967d851db47132b762ce6f')
sha256sums=('f85034ee98c8ca07fb3cd826142c1cd1e1e5747075a94c75a45783bbc4fe2deb')

prepare() {
  # skip tests that require AWS or GCS
  sed -i '/skip_without_.*_credentials <- function()/a\ \ skip("AWS/GCS test")' \
      "$_pkgname/tests/testthat/helper.R"
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
