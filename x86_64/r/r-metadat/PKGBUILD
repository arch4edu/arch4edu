# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metadat
_pkgver=1.4-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
  r-bayesmeta
  r-ellipse
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('dc78d17834617fbd29c1b5574532b157')
b2sums=('2a6263df5f3e6c3830670315e839afdb5904767d8818641aebf2ad863adce04833d2130fa05ef8d83f18a0d7183c6fe50099f958f45e8f522606a7f8d2adcb0b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
