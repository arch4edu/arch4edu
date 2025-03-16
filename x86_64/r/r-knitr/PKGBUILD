# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=knitr
_pkgver=1.50
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
  r-litedown
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
md5sums=('b58c37c2d9123ba4a98b1e838da9ac75')
b2sums=('28c461406c5b5a2e590e3417079ca9971382d88fd2d9d09e8d395723f89905e1d7be9678ac77c912eeed17ad69915d86c4ec382dfcf0d07837495fd83a7a18f8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
