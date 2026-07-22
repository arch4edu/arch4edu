# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mvnfast
_pkgver=0.2.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Fast Multivariate Normal and Student's t Methods"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  lapack
  r-rcpp
)
makedepends=(
  r-bh
  r-rcpparmadillo
)
optdepends=(
  r-knitr
  r-microbenchmark
  r-mvtnorm
  r-plyr
  r-rhpcblasctl
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7f86b01f428f34145a2fd143b441e9bf')
b2sums=('47e120c7d1345828f1a3cff881c41229c9c17d1d435d103aa692cab54b6d3acd6a8507c1e816f7d0a8f4332ad0cca9f29ccb1ea4c979c801eeb1f4095f3eb214')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
