# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=knitr
_cranver=1.41
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="A General-Purpose Package for Dynamic Report Generation in R"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(
    r-evaluate
    r-highr
    r-stringr
    r-yaml
    r-xfun
)
optdepends=(
    r-markdown
    r-formatr
    r-testit
    r-digest
    r-rgl
    r-rmarkdown
    r-htmlwidgets
    r-webshot
    r-tikzdevice
    r-tinytex
    r-reticulate
    r-juliacall
    r-magick
    r-png
    r-jpeg
    r-gifski
    r-xml2
    r-httr
    r-dbi
    r-showtext
    r-tibble
    r-sass
    r-bslib
    r-ragg
    r-gridsvg
    r-styler
    r-targets
    'pandoc: R Markdown v2 and reStructuredText support'
    'rst2pdf: rst2pdf() support'
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('01295f2938509d76474c1637a4260950194a4bae35a9463a07823d6b4a0dfbc7')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
