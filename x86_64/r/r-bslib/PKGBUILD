# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=bslib
_pkgver=0.10.0
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
  r-brand.yml
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
md5sums=('63fd55ca6856c3c55d65e2fe5ccd2cd2')
b2sums=('591127b27f6ceba0aaefdd403533c1b206c2853fc2ebf9feeb50240a9189a1319dca93440ebbd7b538b9ca55b97a1faf3bde642c5d873e4d35d4543523eaaff9')

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
