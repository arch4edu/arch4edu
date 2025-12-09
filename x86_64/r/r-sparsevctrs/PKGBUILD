# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=sparsevctrs
_pkgver=0.3.5
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
md5sums=('9e38bba29a54dcac756d91eb65dcd208')
b2sums=('204224c054f8b113ff8c710f6061293d1f179b3b2b88a8b0e8526d0105c2e64bb8c6b5e655b177dafd1d658e1fee5f7e4e85b7c763c8674ebab04c48e10c6f40')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

}
