# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: anzi2001 <anzi2001 at gmail dot com>
# Contributor: haha662 <haha662 at outlook dot com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=rmarkdown
_pkgver=2.30
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
md5sums=('65deca50090adfd5f6ab55f3a6bed89e')
b2sums=('43ea0065dc47d24030c91270ba3e2b23cdd1f074ce2f6dcbc0fc29eebe0aa68987ae7e2ea3b1527c78fe79c0094168d115d18c62ccf441442f0a79b0ba7be374')

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
