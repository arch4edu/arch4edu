# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clock
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Date-Time Types and Tools"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-cli
  r-lifecycle
  r-rlang
  r-tzdb
  r-vctrs
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-slider
  r-testthat
)
optdepends=(
  r-covr
  r-knitr
  r-magrittr
  r-pillar
  r-rmarkdown
  r-slider
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d28202660aa1adbc17c996def84ad6d8')
sha256sums=('54e57a3b3f8c308d67536e2a75d48f3493cf7fe821bfa4da9159b4fb2ceca874')

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
