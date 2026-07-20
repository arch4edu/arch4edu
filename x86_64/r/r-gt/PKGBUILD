# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gt
_pkgver=1.3.0
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
md5sums=('81c2eb281461bb8423faaca8dbd1b640')
b2sums=('5b259e1f6f6117a9db1a81f46b2c80e5acd6b5fed5888aad32e23caef1821ed49e55ef304ca48357620dbdca08eee2422567ed801d082ea62f7a396bf6a5ef79')

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
