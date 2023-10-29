# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=tibble
_pkgver=3.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=5
pkgdesc="Simple Data Frames"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
sha256sums=('65a72d0c557fd6e7c510d150c935ed6ced5db7d05fc20236b370f11428372131')

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
