# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=shiny
_pkgver=1.8.1
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
  r-future
  r-ggplot2
  r-testthat
  ttf-font
)
optdepends=(
  r-cairo
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
md5sums=('2ca63a8d9ecc6127c155366d8ef6929c')
b2sums=('c63019aaae28b9357dc021c023a920dfca58c35183c644c3c9896912751218a2f6d7cf44a91f418983df2bc8cbfa9cb971bd0938502314e42d1dad97efac458d')

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
