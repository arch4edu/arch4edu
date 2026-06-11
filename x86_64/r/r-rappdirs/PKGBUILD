# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=rappdirs
_pkgver=0.3.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Application Directories: Determine Where to Save Data, Caches, and Logs"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
checkdepends=(
  r-testthat
  r-withr
)
optdepends=(
  r-covr
  r-roxygen2
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('a990a3ddcfa9eb422cd406f78084fbd8'
         '86106366bdf6586bb505dcc53dcc1ba2')
b2sums=('79c6b99127304654d1c3c1c5fd882c8170f22c5d9554c0ed6f38b1c633fbc22948204d8684d39de3e4ecd67f80af29b0fb2bc5e7b8bf78689ed0d9cc625654c6'
        'a8b98e83b9cafdf1117627c99c13ec5fb2b05176d8c031e07eb888230e23d3a280308d8012c0dbf0312b22f83eca522f249155dfef0d8dd4855b4a7512e6d3e5')

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
