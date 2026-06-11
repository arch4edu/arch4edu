# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=spaMM
_pkgver=4.6.65
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Mixed-Effect Models, with or without Spatial Random Effects"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('CECILL-2.0')
depends=(
  gsl
  r-backports
  r-cli
  r-geometry
  r-gmp
  r-minqa
  r-nloptr
  r-numderiv
  r-pbapply
  r-proxy
  r-rcpp
  r-reformulas
  r-roi
)
makedepends=(
  r-rcppeigen
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-agridat
  r-blackbox
  r-fmesher
  r-foreach
  r-future
  r-future.apply
  r-infusion
  r-isorix
  r-lme4
  r-maps
  r-multilevel
  r-rann
  r-rcdd
  r-roi.plugin.glpk
  r-rsae
  r-rspectra
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-LICENSE::http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt")
md5sums=('763b6aa0eb6ae94f5f9899112c931393'
         '599cf91b33571e942d3ba5f9623b8011')
b2sums=('7c592f3da7f5d3dcfe64692efd5e04d6e27394d6afbf141909af62e5beec5ff5fefa85c3c2ca53e46422b2c3ece68f01dc0c3b97ae91db95cf3ac825f988c5be'
        'ff97dacc39b8597e670dbaf5bc0f0e4db73eada273708433fc227fa72c054a30a67dbc7b2416089d68f09ab65da721e5b30711022c41047d9cf706731d568038')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 "$_pkgname-LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
