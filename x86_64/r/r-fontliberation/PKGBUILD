# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fontLiberation
_pkgver=0.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Liberation Fonts"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(custom:OFL)
depends=(
  r
  ttf-liberation
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7a317aca78d58fc0b2417380cc702864')
sha256sums=('acdea423e005873aa509e280074a3cef4796e4f7e9d77b3945d77b451ea039f0')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"

  # symlink TTF fonts to ttf-liberation package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/fonts/liberation-fonts"
  local _font
  for _font in *.ttf; do
    ln -sf "/usr/share/fonts/liberation/$_font"
  done
}
