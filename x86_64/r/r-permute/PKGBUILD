# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=permute
_pkgver=0.10-0
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
md5sums=('adeaa5f1517f5de7fab9df51d7c90bb1')
b2sums=('82d0a85800906904a75a5dd580a91d43c21acb27ca7f89c6a748a00bcd0eddbef757eed5f6d90ddd2e32ca297b52182683ee9d86444106c168cecf870bea34d0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
