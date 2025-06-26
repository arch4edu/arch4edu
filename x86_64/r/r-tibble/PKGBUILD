# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=tibble
_pkgver=3.3.0
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
md5sums=('d7ae660898db86c72a6996d150c19180')
b2sums=('3fecc81e292a6948b7b650fb6d231427680ce72521509ccc7fb8dd181b83aff09ccd2a956ee4cbb280176901b37623687f23c412e9b32a49466c67a466f215a6')

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
