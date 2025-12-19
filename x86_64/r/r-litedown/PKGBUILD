# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=litedown
_pkgver=0.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc="A Lightweight Version of R Markdown"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r-commonmark
  r-xfun
)
optdepends=(
  r-rbibutils
  r-rstudioapi
  r-tinytex
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('66459fa5112e91920a950fa10e3ae188')
b2sums=('e0bb1d72507818cd94f14d9d865124b7afee8c7b29ab7464cf9175144453f87f603e69d84abac27cc1bfd24017c991a84503d9e9037d234200559845f4431e3c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
