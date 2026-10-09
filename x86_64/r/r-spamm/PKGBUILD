# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=spaMM
_pkgver=4.7.17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Mixed-Effect Models, with or without Spatial Random Effects"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('CECILL-2.0')
depends=(
  r-backports
  r-cli
  r-geometry
  r-gmp
  r-matrixstats
  r-minqa
  r-nloptr
  r-numderiv
  r-pbapply
  r-proxy
  r-rcpp
  r-reformulas
  r-roi
  gsl
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
  r-knitr
  r-lme4
  r-maps
  r-multilevel
  r-rann
  r-rcdd
  r-rmarkdown
  r-roi.plugin.glpk
  r-rsae
  r-rspectra
  r-testthat
  r-tweedie
  r-tweediedistr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-LICENSE::http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt")
md5sums=('88b622a54a260c7c2bd19ade419751f7'
         '599cf91b33571e942d3ba5f9623b8011')
b2sums=('c6019526a8eb62d55a6359db04e988e82fa02f4bc735082dd701912a562499315f1ef7c054154be5d0c3907ef049b5b09527b8ca32776c729abcc18129734af9'
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
