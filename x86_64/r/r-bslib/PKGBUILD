# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=bslib
_pkgver=0.6.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-base64enc
  r-cachem
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
md5sums=('688035c1317d99324ef73bb5100664b1')
sha256sums=('642735afd7d3895f1ac8c5a5f7f5e08001bfabcf62a56d2d85904655a2e931db')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
