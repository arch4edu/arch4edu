# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fontBitstreamVera
_pkgver=0.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Fonts with 'Bitstream Vera Fonts' License"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(custom)
depends=(
  r
  ttf-bitstream-vera
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c32821c06d909336ace68f2df3d8710e')
sha256sums=('3298b3dd95605bdda0c5fce5594c9bedde6aa63d89b216d5c83c6c092b6d375a')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENCE" "$pkgdir/usr/share/licenses/$pkgname"

  # symlink TTF fonts to ttf-bitstream-vera package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/fonts/bitstream-vera-fonts"
  local _font
  for _font in *.ttf; do
    ln -sf "/usr/share/fonts/TTF/$_font"
  done
}
