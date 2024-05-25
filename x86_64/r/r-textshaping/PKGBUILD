# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=textshaping
_pkgver=0.4.0
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
md5sums=('fac64803fa2677b0a346851d7b076e11')
b2sums=('23d09aaaa56d1fa0f6a8f6bb79ef3b76dadd348fd0306af24b6658beef28d602aaa48524f49d473443d2eb237a2ab2b3e8f4db633179fdb49e12a4c8cea457e4')

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
