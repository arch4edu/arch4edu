# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=optimx
_pkgver=2024-12.2
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
md5sums=('657a8a621309a287fd94eb8d67d1a77d')
b2sums=('54699da9cd4476bb5af9c62b75507d4af9b427fe7d581a11486b105aed193663b08448b83a189ab6ec6f4cbfa989a2d9f4480b5fd2b218ba48b926e92cdc10e6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
