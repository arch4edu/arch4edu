# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dfidx
_pkgver=0.1-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Indexed Data Frames"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-dplyr
  r-formula
  r-glue
  r-pillar
  r-rdpack
  r-tidyselect
  r-vctrs
)
optdepends=(
  r-knitr
  r-quarto
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c6a7f74c8ea9d86c5ba078e73bc98cf3')
b2sums=('883f1f458d663448ddeb30d06ba792f43d7dfb0128090dd51dbc4c5145be6581e7a0c35bb17f46a2bd3af38fd89a90a649c6d7554152f63674f11f1e56b75acf')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
