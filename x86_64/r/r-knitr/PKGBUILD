# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=knitr
_pkgver=1.46
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A General-Purpose Package for Dynamic Report Generation in R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
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
  r-svglite
  r-targets
  r-testit
  r-tibble
  r-tikzdevice
  r-tinytex
  r-webshot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ac4eae7a57b7ff78c5bd3faf76d4ec04')
b2sums=('3b6b4c08b47ad40519c8c36af4d7e4d625665f998b23bd75cdc618411141dd0466372ea8e2c11ea2a7d2938e79ba6a43b4da77575141fec9bf95761047ce401c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
