# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=glue
_pkgver=1.6.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=9
pkgdesc="Interpreted String Literals"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r
)
optdepends=(
  r-covr
  r-crayon
  r-dbi
  r-dplyr
  r-forcats
  r-ggplot2
  r-knitr
  r-magrittr
  r-microbenchmark
  r-r.utils
  r-rmarkdown
  r-rprintf
  r-rsqlite
  r-stringr
  r-testthat
  r-vctrs
  r-waldo
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4a92a6b8f8015a2ac8b0bfeac7f163fc')
sha256sums=('9da518f12be584c90e75fe8e07f711ee3f6fc0d03d817f72c25dc0f66499fdbf')

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
