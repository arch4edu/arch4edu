# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gt
_pkgver=1.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Easily Create Presentation-Ready Display Tables"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-base64enc
  r-bigd
  r-bitops
  r-cli
  r-commonmark
  r-dplyr
  r-fs
  r-glue
  r-htmltools
  r-htmlwidgets
  r-juicyjuice
  r-magrittr
  r-markdown
  r-reactable
  r-rlang
  r-sass
  r-scales
  r-tidyselect
  r-vctrs
  r-xml2
)
optdepends=(
  r-bit64
  r-farver
  r-fontawesome
  r-ggplot2
  r-gtable
  r-katex
  r-knitr
  r-lubridate
  r-magick
  r-officer
  r-paletteer
  r-rcolorbrewer
  r-rmarkdown
  r-rsvg
  r-rvest
  r-shiny
  r-testthat
  r-tidyr
  r-webshot2
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2d4dcb3e8fed11257adeb7b0514dd030')
b2sums=('6db2b328a941d9c610ba65d3da35f917b84834039b605aeb7eec4e47c425ec5985b0e9fc82c84253d6441fb55a3c9a8f127f91a57722e3dee8176ee21e5a2fc4')

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
