# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=optimx
_pkgver=2025-4.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('8f224b177cc716ef40c907af54b55d7d')
b2sums=('80b76805f920069a5bf336a7b8b6ba3cb188bb1de459dfcbf2d32f2652e9715d68965d94ebf2a7d96c2f55279febcb7c5db5cf29fc7b1d70152fb487430e265e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
