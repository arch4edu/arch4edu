# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fontLiberation
_pkgver=0.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Liberation Fonts"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('OFL-1.1-RFN')
depends=(
  r
  ttf-liberation
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7a317aca78d58fc0b2417380cc702864')
b2sums=('6c01af50df129aaed422f328af0a75b2041a4f6e844c9d3a39fd79473d15fb48e1d9d864082c9abe4d5ca74bdd8f7e5f0a577732af42ac075f59c071e442ffcf')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
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
