# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=GGally
_pkgver=2.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extension to 'ggplot2'"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-dplyr
  r-ggplot2
  r-ggstats
  r-gtable
  r-lifecycle
  r-magrittr
  r-plyr
  r-progress
  r-rcolorbrewer
  r-rlang
  r-scales
  r-tidyr
)
checkdepends=(
  r-chemometrics
  r-crosstalk
  r-geosphere
  r-ggforce
  r-hmisc
  r-intergraph
  r-mapproj
  r-maps
  r-network
  r-sna
  r-testthat
  r-vdiffr
)
optdepends=(
  r-broom
  r-broom.helpers
  r-chemometrics
  r-crosstalk
  r-emmeans
  r-geosphere
  r-ggforce
  r-hmisc
  r-igraph
  r-intergraph
  r-knitr
  r-labelled
  r-mapproj
  r-maps
  r-network
  r-rmarkdown
  r-roxygen2
  r-scagnostics
  r-sna
  r-spelling
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ba770293c7c59d282359e9425e0c3f7b')
sha256sums=('dce20b47d639aa1ad63d9f14aae48c554d1e787758876c9842bf0e093bab80dd')

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
}
