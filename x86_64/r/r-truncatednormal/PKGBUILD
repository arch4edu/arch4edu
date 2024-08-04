# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=TruncatedNormal
_pkgver=2.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Truncated Multivariate Normal and Student Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  blas
  lapack
  r-alabama
  r-nleqslv
  r-qrng
  r-rcpp
  r-spacefillr
)
makedepends=(
  r-rcpparmadillo
)
optdepends=(
  r-cardata
  r-knitr
  r-mvtnorm
  r-rmarkdown
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c19c441146bd9cf9b4732fc42a26816a')
b2sums=('1313a2add6ed3540ba72ffb6e06491b3e2fccb1a3cafbfe8b6abbba388ec1233c59b3eddf732cfdfd4d39a69a22a9598125edc7a55931363112b603870251210')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
