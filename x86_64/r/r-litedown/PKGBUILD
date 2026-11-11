# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=litedown
_pkgver=1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc="A Lightweight Version of R Markdown"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r-xfun
)
optdepends=(
  r-rbibutils
  r-rstudioapi
  r-testit
  r-tinyimg
  r-tinytex
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b232b14ae798884872f294bc369fa12b')
b2sums=('c4fe520257ef1b3a2380dea77e5266160dd28ed2d184fea364dc0e5a9ef1b8eae9dc9ea32d03753c6162b242ee625d594e73f443875cf08b87b56d5460f2d258')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
