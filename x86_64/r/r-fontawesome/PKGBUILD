# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=fontawesome
_pkgver=0.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
  r-knitr
  r-rsvg
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d5e7d3d788f1145dd8cb5b74c85045b9')
b2sums=('d8a2b16425bc6aaf767526f2372981243a524ff60cfa6527dc9ff930ee5d5f9a15a10935a19a4ea76105277af8d7b8e44f7a13e80ac041a8c702fe5309104e2b')

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
