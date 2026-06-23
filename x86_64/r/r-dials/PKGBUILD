# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dials
_pkgver=1.4.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Creating Tuning Parameter Values"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dicedesign
  r-dplyr
  r-glue
  r-hardhat
  r-lifecycle
  r-pillar
  r-purrr
  r-rlang
  r-scales
  r-sfd
  r-tibble
  r-vctrs
  r-withr
)
checkdepends=(
  r-kernlab
  r-testthat
  r-xml2
)
optdepends=(
  r-covr
  r-ggplot2
  r-kernlab
  r-knitr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('32ef415f6f0fbfd32f232128c59507af')
b2sums=('b69077d19dbedfb45e946e845ccad7fd0963016c77f730365c640fd6edf0ada6981caaf93a3f6f965dd8a7f9e06f713791b7d29aecacde85476c4060ab7ab246')

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
