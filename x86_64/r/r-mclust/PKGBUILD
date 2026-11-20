# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mclust
_pkgver=6.1.4
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
md5sums=('02aaeaf4337a3c1f2e45e300db4434de')
b2sums=('9b83697db6c8d9fc791cdbbd4a488141c5622ad9fedf99811f4130a09f75f91e015b10b84a181d32e92427cf6babada8fb3d565de4d5adf7d228a99cce6c90e6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
