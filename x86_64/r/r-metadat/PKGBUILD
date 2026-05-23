# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metadat
_pkgver=1.6-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Meta-Analysis Datasets"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-mathjaxr
)
optdepends=(
  r-ape
  r-bayesmeta
  r-biasedurn
  r-clubsandwich
  r-dfoptim
  r-digest
  r-ellipse
  r-gridextra
  r-igraph
  r-lme4
  r-mada
  r-meta
  r-metafor
  r-metasens
  r-mvtnorm
  r-netmeta
  r-numderiv
  r-rms
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f0f890d4022dae7c6af02323ef51956c')
b2sums=('118c751fd5d6822140987e791a94b8d2e996d42ff00ef898bc5c1222044951b938515718266e4a5b7212b7c5e71e116391d86e555c1406c456c0af7044ac9458')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
