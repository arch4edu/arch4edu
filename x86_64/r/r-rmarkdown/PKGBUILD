# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: anzi2001 <anzi2001 at gmail dot com>
# Contributor: haha662 <haha662 at outlook dot com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=rmarkdown
_pkgver=2.27
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Dynamic Documents for R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  pandoc
  r-bslib
  r-evaluate
  r-fontawesome
  r-htmltools
  r-jquerylib
  r-jsonlite
  r-knitr
  r-tinytex
  r-xfun
  r-yaml
)
checkdepends=(
  r-curl
  r-shiny
  r-testthat
  r-xml2
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
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8eba2269baef8019b571ec136c579f83')
b2sums=('d140882cae4ded188615e6c21b77e763db61bb52e1617b2ec599d088b12dc1015e86f0a143a9796159722749ad3c5d88e5015f3a8661dacb38253f3bd1112f92')

prepare() {
  # Skip a test that might fail depending on environment
  sed -i '/"Converting bib file is working"/a\ \ skip("Inconsistent test")' \
      "$_pkgname/tests/testthat/test-pandoc.R"
}

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
}
