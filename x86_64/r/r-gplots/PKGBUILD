# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gplots
_pkgver=3.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Various R Programming Tools for Plotting Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-catools
  r-gtools
)
optdepends=(
  r-knitr
  r-r2d2
  r-rmarkdown
  r-dendextend
  r-heatmaply
  r-rcolorbrewer
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3271bbd55b49779d3d27ef542480e6ea')
b2sums=('7abc40f659b401c315099682fdd3efbaf4d9cad8cdf9d5c61cfe54c749d00dec32e251139d853a611d87c72df974a8a6be75e27b258aa32cc2bfb4de69b9ef28')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
