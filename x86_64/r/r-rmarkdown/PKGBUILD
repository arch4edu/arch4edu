# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: anzi2001 <anzi2001 at gmail dot com>
# Contributor: haha662 <haha662 at outlook dot com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=rmarkdown
_pkgver=2.24
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Dynamic Documents for R"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  pandoc
  r-bslib
  r-evaluate
  r-fontawesome
  r-htmltools
  r-jquerylib
  r-jsonlite
  r-knitr
  r-stringr
  r-tinytex
  r-xfun
  r-yaml
)
checkdepends=(
  r-curl
  r-shiny
  r-testthat
  texlive-basic
  texlive-fontsrecommended
  texlive-latexextra
)
optdepends=(
  r-cleanrmd
  r-digest
  r-downlit
  r-dygraphs
  r-fs
  r-katex
  r-rsconnect
  r-sass
  r-shiny
  r-testthat
  r-tibble
  r-vctrs
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c96192e4ab4c47afdce5fb29fa83fabc')
sha256sums=('3873efa46df4b1d2613b49d345d6442cd1a332e08594c204c8fa177edcd53d86')

prepare() {
  # Skip a test that might fail depending on environment
  sed -i '/"Converting bib file is working"/a\ \ skip("Inconsistent test")' \
      "$_pkgname/tests/testthat/test-pandoc.R"
}

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
