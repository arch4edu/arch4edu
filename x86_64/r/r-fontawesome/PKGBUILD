# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=fontawesome
_pkgver=0.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Easily Work with 'Font Awesome' Icons"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
sha256sums=('da3de2a9717084d1400d48edd783f06c66b8c910ce9c8d753d1b7d99be1c5cc9')

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

  # symlink TTF fonts to ttf-font-awesome package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/fontawesome/webfonts"
  local _font
  for _font in *.ttf; do
    ln -sf "/usr/share/fonts/TTF/$_font"
  done
}
