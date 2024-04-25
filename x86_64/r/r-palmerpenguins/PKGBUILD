# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=palmerpenguins
_pkgver=0.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Palmer Archipelago (Antarctica) Penguin Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('CC0-1.0')
depends=(
  r
)
optdepends=(
  r-dplyr
  r-ggplot2
  r-knitr
  r-recipes
  r-rmarkdown
  r-tibble
  r-tidyr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('dff628ed0c5f7b8e265127221491934e')
b2sums=('55db3d0bd451dace7d71328e55a8477ca0ecd40067d92b13fb1d9f6d3957cd3cc75118191acc12bb2d707099d45642eec8918a5e098a72ba8c5aeca635b43267')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
