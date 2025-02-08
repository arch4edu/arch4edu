# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=bslib
_pkgver=0.9.0
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
  r-yaml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b36702a77f5e310bd44f36d6604ed2c5')
b2sums=('189f06b92b647d592bd285d65ab8683c9ebf0f66b1c1e3db26dc1b79de5489b0299fe30e3e7cd59269b7ef3b683e142b932f4b0aac3612c0096d2677bcae62fd')

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
