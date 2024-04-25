# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=tibble
_pkgver=3.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Simple Data Frames"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-fansi
  r-lifecycle
  r-magrittr
  r-pillar
  r-pkgconfig
  r-rlang
  r-vctrs
)
optdepends=(
  r-bench
  r-bit64
  r-blob
  r-brio
  r-callr
  r-cli
  r-covr
  r-crayon
  r-diagrammer
  r-dplyr
  r-evaluate
  r-formattable
  r-ggplot2
  r-here
  r-hms
  r-htmltools
  r-knitr
  r-lubridate
  r-mockr
  r-nycflights13
  r-pkgbuild
  r-pkgload
  r-purrr
  r-rmarkdown
  r-stringi
  r-testthat
  r-tidyr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e4ccfbe28c84b11f86388379c8b43925')
b2sums=('7368a112ee6729736610a44acdbdc651fb786635d7126c88fe0aa1ccac669feba014fce2b1de15e63faf6f34651885855bd659138a339661660012c8b3ef443c')

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
