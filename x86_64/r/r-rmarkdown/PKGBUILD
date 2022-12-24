# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: anzi2001 <anzi2001 at gmail dot com>
# Contributor: haha662 <haha662 at outlook dot com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=rmarkdown
_cranver=2.19
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Dynamic Documents for R"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(
    pandoc
    r-bslib
    r-evaluate
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
    texlive-core
    texlive-latexextra
    ttf-font
)
optdepends=(
    r-digest
    r-dygraphs
    r-fs
    r-rsconnect
    r-downlit
    r-katex
    r-sass
    r-shiny
    r-testthat
    r-tibble
    r-tufte
    r-vctrs
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('39c2a4c51de8c65886a7a3d7e44c3d21167069a89ee26c0f5db8243b70db9b92')

prepare() {
  # Skip a test that might fail depending on environment
  sed -i '/"Converting bib file is working"/a\ \ skip("Inconsistent test")' \
      "${_cranname}/tests/testthat/test-pandoc.R"
}

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
