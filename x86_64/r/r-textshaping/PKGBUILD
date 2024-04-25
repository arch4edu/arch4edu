# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=textshaping
_pkgver=0.3.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Bindings to the 'HarfBuzz' and 'Fribidi' Libraries for Text Shaping"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  freetype2
  fribidi
  harfbuzz
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
md5sums=('75e150aec896dd1807e84538456d22e3')
b2sums=('d6f9c061e9ffcc8e58e423cf4e1b8e07ca9873122d682fbddb03bb73b068770cc2aa750dc871948f25d0af0a28a6fcdf643c3974d1c5ca3c70b09eb28814c45b')

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
