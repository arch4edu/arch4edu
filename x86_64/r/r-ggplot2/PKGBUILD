# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>
# Contributor: Tobias Neumann <mail at tobias dash neumann dot eu>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=ggplot2
_pkgver=3.5.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Create Elegant Data Visualisations Using the Grammar of Graphics"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-glue
  r-gtable
  r-isoband
  r-lifecycle
  r-rlang
  r-scales
  r-tibble
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
  r-sf
  r-svglite
  r-testthat
  r-vdiffr
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-fix-snapshots.patch::https://github.com/tidyverse/ggplot2/pull/5917/commits/7908e224e03fce65ce910cd85f3de3b2846970d6.patch")
md5sums=('f2add92370293ac6078f1963427d6ab2'
         'c1beb06c438ec674a22babfb6ca987a8')
b2sums=('6082e08ffed5d945d444890c5ef6084ed477a4e7db70c23a02ff0664571a7ca8d1c74c06c77a3aff5ff6913505ab5a6cf116f310ab78d7c3d63583c948587b78'
        'b01d6fd2c0d251fa64792fa22ccd7627f44d2cd9e1d11b3b4c085244fa14fcc074a07e9106d301e25cd51532f23e65536045e173a1c061d1d51732d0ee80a670')

prepare() {
  # update test snapshots
  patch -Np1 -d "$_pkgname" < "$_pkgname-fix-snapshots.patch"
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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
