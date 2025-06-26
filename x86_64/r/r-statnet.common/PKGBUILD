# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statnet.common
_pkgver=4.12.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Common R Scripts and Utilities Used by the Statnet Project Software"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-coda
)
optdepends=(
  r-covr
  r-rlang
  r-roxygen2
  r-purrr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d74055cfddeadb4843750b746ba18af1')
b2sums=('125e97ba814d92535197c44b0ee6339a6daa6ce93dd6e7328c6ac09d28d43c5373af1056b7af121ac406eb5f5da3915615ecb675c46e3d651ba5317af46894a9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
