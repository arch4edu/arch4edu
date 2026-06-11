# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=tibble
_pkgver=3.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Simple Data Frames"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
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
  r-nycflights13
  r-pkgload
  r-purrr
  r-rmarkdown
  r-stringi
  r-testthat
  r-tidyr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('97ff25ebdd1460ec152d48e9bb54fa43')
b2sums=('6e59dc555e0177085d34d3e1d876f7967dc47b9cb9fb11585c8c21ab13cf8ca1940d1172bf76d4b039a40d268718cfab86049299054ca1a82c803a42b6fcdf7c')

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
