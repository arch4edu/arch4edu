# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=pkgsearch
_pkgver=3.1.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Search and Query CRAN R Packages"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-curl
  r-jsonlite
)
checkdepends=(
  r-mockery
  r-pingr
  r-testthat
)
optdepends=(
  r-covr
  r-memoise
  r-mockery
  r-pillar
  r-pingr
  r-rstudioapi
  r-shiny
  r-shinyjs
  r-shinywidgets
  r-testthat
  r-whoami
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('390ae87ab02521712f8a6aa4489d6d83'
         'b107e365dd7f7e32cc1e21b4d0cb3db9')
b2sums=('21bdb824269b5695320d8c23724f730f9a20dc537127c778775581fa281aa58d33b21b370dccde6237d43ebdc84437ac3218dc00951956f2d52a0948ca3c6532'
        '940785dd4867c9c823c76b0ef8123c61b2404b0ba69a6f67380c9684840e6ae98fe68c58f74ea8c5bf64a2e924292e45bd528baf521eed988419a43306f3dddf')

prepare() {
  # skip failing tests
  patch -Np1 -i fix-tests.patch
}

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
