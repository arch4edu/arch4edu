# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>

_pkgname=mvtnorm
_pkgver=1.5-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multivariate Normal and t Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  blas
  lapack
  r-bibtex
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-numderiv
  r-qrng
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('039cbb95c4c11960cf87fdecf26ee510')
b2sums=('23668d80daacb1f86109e5923d3a2727eba070186650a0c9149f68bc7e654b2264aa2b50f572e5d77537b28b661b8cc1df9ef311d37cbe03b1a96cece44b31a3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
