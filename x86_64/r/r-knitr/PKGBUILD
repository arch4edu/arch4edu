# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=knitr
_pkgver=1.48
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
md5sums=('230565deedd16f98e50aea9bb083abe6')
b2sums=('b480acb9dff1029eaca5534ad1868158bf7bd0a5ba892ecdf9f9e669cdb42c6f0d611ee892c285a92cbf56aebc1fb511e1cd2659e0af4e413551454d7e785b17')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
