# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=permute
_pkgver=0.9-10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Functions for Generating Restricted Permutations of Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-bookdown
  r-knitr
  r-rmarkdown
  r-sessioninfo
  r-testthat
  r-vegan
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a6bd560a04d3df99268d5f3255477837')
b2sums=('f568abe6fd62ddc954c941d872bfc8a6f6b153a4f497310965af138677c600d2be277eb50fc6b6a25e456ade672cc5783586ffd17db66eadeb8cb39f272c00fb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
