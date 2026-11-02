# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=sparsevctrs
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc='Sparse Vectors for Use in Data Frames'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r-cli
  r-rlang
  r-vctrs
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
  r-tibble
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1d8585530914996ac0d36b071e27bda5')
b2sums=('530d0fd35e0634053296e7ff8421805c521b4f869cabfef2e3dc0e19b7fcb9456c9b4b06923f1ccc37d83090aa9db34ec220459b195caa606df7bb2aacf61d3c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

}
