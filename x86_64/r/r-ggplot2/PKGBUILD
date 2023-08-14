# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_pkgname=ggplot2
_pkgver=3.4.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Create Elegant Data Visualisations Using the Grammar of Graphics"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
  r-maptools
  r-multcomp
  r-munsell
  r-profvis
  r-quantreg
  r-ragg
  r-rcolorbrewer
  r-rgeos
  r-rmarkdown
  r-sf
  r-svglite
  r-testthat
  r-vdiffr
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('56b406dd3fa5a2839fac8415a7a1b6e1')
sha256sums=('5ce29ace6be7727be434506a1c759dfc322f65b17eabeec863b93be10f91a543')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
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
