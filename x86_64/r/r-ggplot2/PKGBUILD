# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>
# Contributor: Tobias Neumann <mail at tobias dash neumann dot eu>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=ggplot2
_pkgver=4.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Create Elegant Data Visualisations Using the Grammar of Graphics"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-gtable
  r-isoband
  r-lifecycle
  r-rlang
  r-s7
  r-scales
  r-vctrs
  r-withr
)
checkdepends=(
  r-hexbin
  r-mapproj
  r-quantreg
  r-sf
  r-sp
  r-svglite
  r-testthat
  r-xml2
  ttf-font
)
optdepends=(
  r-broom
  r-covr
  r-dplyr
  r-ggplot2movies
  r-hexbin
  r-hmisc
  r-knitr
  r-mapproj
  r-maps
  r-multcomp
  r-munsell
  r-profvis
  r-quantreg
  r-ragg
  r-rcolorbrewer
  r-rmarkdown
  r-roxygen2
  r-sf
  r-svglite
  r-testthat
  r-tibble
  r-vdiffr
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-fix-snapshots.patch::https://github.com/tidyverse/ggplot2/pull/5917/commits/7908e224e03fce65ce910cd85f3de3b2846970d6.patch")
md5sums=('22eb62f9579e90530b2841626c9ec8d6'
         'c1beb06c438ec674a22babfb6ca987a8')
b2sums=('34d5961c7860e01f010318f46b5470b435ac06f23a78154b534746bd50691b5653b6b54abcab3f4103df6ac9b539e166b17a6b97f3f41f48269fd4173b56e9c3'
        'b01d6fd2c0d251fa64792fa22ccd7627f44d2cd9e1d11b3b4c085244fa14fcc074a07e9106d301e25cd51532f23e65536045e173a1c061d1d51732d0ee80a670')

#prepare() {
  # update test snapshots
#  patch -Np1 -d "$_pkgname" < "$_pkgname-fix-snapshots.patch"
#}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

#check() {
#  cd "$_pkgname/tests"
#  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
#}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
