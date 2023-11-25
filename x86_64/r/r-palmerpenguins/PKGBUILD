# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=palmerpenguins
_pkgver=0.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Palmer Archipelago (Antarctica) Penguin Data"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
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
sha256sums=('2a40d48ba6c7978fdf2a6daf647ccb39cd17590680138931d11194d3dd1a30b4')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
