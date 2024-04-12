# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metadat
_pkgver=1.2-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Meta-Analysis Datasets"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-mathjaxr
)
optdepends=(
  r-ape
  r-biasedurn
  r-clubsandwich
  r-dfoptim
  r-digest
  r-gridextra
  r-igraph
  r-lme4
  r-meta
  r-metafor
  r-mvtnorm
  r-netmeta
  r-numderiv
  r-rms
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4303e4a28efd69147f6f95fc939ea5db')
b2sums=('878d52d721e644c73da7692bae40463ca7d30b81a54bf9515a223f5d17b0f653da857077276f7dfffdf5a16e861a5373ab65ab15887be336917244f267746e8b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
