# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=bslib
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-base64enc
  r-cachem
  r-fastmap
  r-htmltools
  r-jquerylib
  r-jsonlite
  r-lifecycle
  r-memoise
  r-mime
  r-rlang
  r-sass
)
optdepends=(
  r-bsicons
  r-curl
  r-fontawesome
  r-future
  r-ggplot2
  r-knitr
  r-magrittr
  r-rappdirs
  r-rmarkdown
  r-shiny
  r-testthat
  r-thematic
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('081e2345dcf8260e89fd196f399e996b')
b2sums=('f895e6038349e0028be7bf8c5956d3bd6fba1dc29a714a6f040ebdf501dbcbb950a5d3c8c3a3dd04e31c95ebf3a3d8b6f38ccc62bc2343811e27a69b883d8712')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
