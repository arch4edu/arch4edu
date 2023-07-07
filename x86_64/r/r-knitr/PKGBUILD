# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=knitr
_pkgver=1.43
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="A General-Purpose Package for Dynamic Report Generation in R"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-evaluate
  r-highr
  r-xfun
  r-yaml
)
optdepends=(
  'pandoc: R Markdown v2 and reStructuredText support'
  'rst2pdf: rst2pdf() support'
  r-bslib
  r-curl
  r-dbi
  r-digest
  r-formatr
  r-gifski
  r-gridsvg
  r-htmlwidgets
  r-jpeg
  r-juliacall
  r-magick
  r-markdown
  r-png
  r-ragg
  r-reticulate
  r-rgl
  r-rlang
  r-rmarkdown
  r-rstudioapi
  r-sass
  r-showtext
  r-styler
  r-targets
  r-testit
  r-tibble
  r-tikzdevice
  r-tinytex
  r-webshot
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('94653f9976f8ea8f6ce183802b2cee73')
sha256sums=('3d29baea8c349aaa9310879ceb9a9d51bcaec39827ad46d422c3793c8a4ed53c')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
