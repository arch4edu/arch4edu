# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=permute
_pkgver=0.9-8
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
md5sums=('81a115d8e646ca0e31df435f242ea11b')
b2sums=('5ea20ffd55258116a3e51039d5ef0c6549ba83fce568b5b82cbc4a3e06c8e6cdfa385dae5b6e7ac6bc397a8664e6df69241054d83f524be5dd956bd284cc2aa5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
