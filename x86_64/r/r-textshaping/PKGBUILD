# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=textshaping
_pkgver=1.0.1
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
  r-stringi
  r-systemfonts
)
makedepends=(
  r-cpp11
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('61da72a677ec91df4b2235ec6317a995')
b2sums=('d35df45b7ae5db796f9253c97e2996eb9d6a39539096db6f8c951e72c7ecc62570b68921c8fd610037899ecf9c6f67e3aea41c1a00a6f72515a033c3e68a963b')

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
