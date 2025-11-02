# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=litedown
_pkgver=0.8
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
md5sums=('48dbd5f56761f1737fc63aa5ef29038c')
b2sums=('733ca05e2ef68bd68c3ccf7fc8286d1b5a2b74a93cff6a44eb63d0331bdf1f1df7285041ba6176134d34796629fe00a02a91b65123d4f702be1270dfc1f53c81')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
