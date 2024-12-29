# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=shiny
_pkgver=1.10.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Web Application Framework for R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only AND MIT AND BSD-3-Clause AND Apache-2.0 AND GPL-2.0-or-later')
depends=(
  r-bslib
  r-cachem
  r-commonmark
  r-crayon
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
  r-coro
  r-future
  r-ggplot2
  r-testthat
  ttf-font
)
optdepends=(
  r-cairo
  r-coro
  r-dt
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
md5sums=('b8a598f6d1289a4cbd338088f119ce75')
b2sums=('7bcb8c77c3b74fdfae0f375e8102e58497e71baa52ab131c54eb24d3bf08986b4656b61a979f8a52b7a6db0a585893aece10e6308ef9b47eee4cb23263a035d0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
