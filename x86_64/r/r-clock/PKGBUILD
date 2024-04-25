# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clock
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Date-Time Types and Tools"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
b2sums=('ab976631c8a6210d82b8532695292e9939852a48945bbf07711d5eb84cebda062ec317895d8a98be9dfaeac6010c0d7a78833d3a81da035c6fb201245ba3dd20')

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
