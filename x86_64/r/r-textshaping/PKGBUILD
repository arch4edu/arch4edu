# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=textshaping
_pkgver=0.4.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bindings to the 'HarfBuzz' and 'Fribidi' Libraries for Text Shaping"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  freetype2
  fribidi
  harfbuzz
  r-lifecycle
  r-systemfonts
)
makedepends=(
  r-cpp11
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a8c547a396384530eceba6c9a5153d12')
b2sums=('1b5783d34aaafe38ce1430e48fd7cfa9e69725c9b981a0bb08d942b09ead9ae10f08d1a31c4b0f842637c79a815458a6e6196607903416536626b86cb148a0c0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
