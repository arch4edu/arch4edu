# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=knitr
_pkgver=1.49
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
md5sums=('fd195b5d3881af92282cd1b23d477923')
b2sums=('0a3aeb13ffb49f7e18baa9aec09e4b6b98549564fda83fb30e899ab57d1ff913db19b5af8c832f97de32b13c9e22de82a9e75e18d2ab689801c738620d68b56a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
