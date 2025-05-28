# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=sparsevctrs
_pkgver=0.3.4
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
md5sums=('63bf2af3a041154cf490790193283de2')
b2sums=('5816550b02b85bb818332f4f410d1304b7eb94721c73523226736b1d524b9a0646e68ad229fc39a69323839a5ac3cdc0f8917716f8f5209d6dc3b395534f36e4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

}
