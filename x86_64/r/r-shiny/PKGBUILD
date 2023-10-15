# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=shiny
_pkgver=1.7.5.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Web Application Framework for R"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r-bslib
  r-cachem
  r-commonmark
  r-crayon
  r-ellipsis
  r-fastmap
  r-fontawesome
  r-glue
  r-htmltools
  r-httpuv
  r-jsonlite
  r-later
  r-lifecycle
  r-mime
  r-promises
  r-r6
  r-rlang
  r-sourcetools
  r-withr
  r-xtable
)
checkdepends=(
  r-future
  r-ggplot2
  r-testthat
  ttf-font
)
optdepends=(
  r-cairo
  r-dygraphs
  r-future
  r-ggplot2
  r-knitr
  r-magrittr
  r-markdown
  r-ragg
  r-reactlog
  r-rmarkdown
  r-sass
  r-showtext
  r-testthat
  r-yaml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9fba1a63a8d0f3fe58e3e9ce1ee89e49')
sha256sums=('2023d91cc8039580752f6ecc5010d4419b7d928724ce5b10b93a3b48e1e6fb46')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
