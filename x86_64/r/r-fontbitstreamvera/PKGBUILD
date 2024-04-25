# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fontBitstreamVera
_pkgver=0.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Fonts with 'Bitstream Vera Fonts' License"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Bitstream-Vera')
depends=(
  r
  ttf-bitstream-vera
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c32821c06d909336ace68f2df3d8710e')
b2sums=('a9a5a0d8db6547a317789150d3e073f604d13c38cf583e14d20ab61659f6dd185b873acf809095245deef10d8dc909b39998eb3755506aebb3b3a5117cf50790')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
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
