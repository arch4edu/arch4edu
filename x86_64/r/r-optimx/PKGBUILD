# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=optimx
_pkgver=2023-10.21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Expanded Replacement and Extension of the 'optim' Function"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
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
sha256sums=('0d732d5604c26af59cfb95b80ed4e226c9c10422e2d82a6cc06b92f9ba6a44b5')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
