# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=fontawesome
_pkgver=0.5.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Easily Work with 'Font Awesome' Icons"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-htmltools
  r-rlang
  ttf-font-awesome
)
checkdepends=(
  r-dplyr
  r-testthat
)
optdepends=(
  r-covr
  r-dplyr
  r-gt
  r-knitr
  r-rsvg
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95b072a27418b962792410dfb21c3d2b')
b2sums=('e6feb424059b90a5a7cb2f40ea0fea123f9d3eda4e18626ef0a13cf716af720227d48d0dad912223317a2e0f2ca6d8a0f55f92bbd8171c6fcd590c867da2b173')

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

  # symlink TTF fonts to ttf-font-awesome package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/fontawesome/webfonts"
  local _font
  for _font in *.ttf; do
    ln -sf "/usr/share/fonts/TTF/$_font"
  done
}
