# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=optimx
_pkgver=2023-10.21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Expanded Replacement and Extension of the 'optim' Function"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-nloptr
  r-numderiv
  r-pracma
)
optdepends=(
  r-bb
  r-dfoptim
  r-knitr
  r-lbfgs
  r-lbfgsb3c
  r-marqlevalg
  r-minqa
  r-r.rsp
  r-rmarkdown
  r-setrng
  r-subplex
  r-testthat
  r-ucminf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6bf0366c13fec66c2c89c848ad3fd9b2')
b2sums=('f353e2d12ed4bcfcb4686055e5dc3d6f21759e2ecf484831dee76691dd57ca739f56b99799915fc40bae54254b1cec556b0d285aa4305fc0522d70cee936d939')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
