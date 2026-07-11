# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=litedown
_pkgver=0.10
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
  r-testit
  r-tinyimg
  r-tinytex
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('96d248854e0275893e575842a9b31d79')
b2sums=('e104a9e633644132a6897afcdc0205da95f48ec3cf9bee2450c69edc46959fdf72abc8016985c070f25dd1e7896e59255b667cc9192a50bf4b856899c89d4ba2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
