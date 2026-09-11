# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LiblineaR
_pkgver=2.10-25
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Predictive Models Based on the LIBLINEAR C/C++ Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-sparsem
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('524842ae5efb13d6ad0dc85d3892ff3d')
b2sums=('88548cdf1800fd1627a0c4f164c5af17cc9a4e572630701622ea51976ee3527271b7b65d9e6fc714db84b6723b55f85d846538e8a10fb0fabb075bb167a615b4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
