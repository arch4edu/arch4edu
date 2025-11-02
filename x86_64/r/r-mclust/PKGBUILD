# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mclust
_pkgver=6.1.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Gaussian Mixture Modelling for Model-Based Clustering, Classification, and Density Estimation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  lapack
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-geometry
  r-knitr
  r-mix
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('51537ab6f40307c473b99ab959aa7cd3')
b2sums=('439daca75cbd081b9adc44251fca44c630b1193b84b71ed95300699428022c9e67d50627237396e141c5e0d306141f3dc6f351927ee55ae806e8411bbc29d8f2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
