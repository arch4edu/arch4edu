# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggdist
_pkgver=3.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualizations of Distributions and Uncertainty"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r-cli
  r-distributional
  r-dplyr
  r-ggplot2
  r-glue
  r-numderiv
  r-quadprog
  r-rcpp
  r-rlang
  r-scales
  r-tibble
  r-tidyselect
  r-vctrs
  r-withr
)
checkdepends=(
  r-beeswarm
  r-fda
  r-fontquiver
  r-forcats
  r-mvtnorm
  r-posterior
  r-purrr
  r-showtext
  r-svglite
  r-sysfonts
  r-testthat
  r-tidyr
  r-vdiffr
)
optdepends=(
  r-beeswarm
  r-broom
  r-covr
  r-cowplot
  r-fda
  r-fontquiver
  r-forcats
  r-knitr
  r-modelr
  r-mvtnorm
  r-palmerpenguins
  r-patchwork
  r-pkgdown
  r-posterior
  r-purrr
  r-rmarkdown
  r-showtext
  r-svglite
  r-sysfonts
  r-testthat
  r-tidyr
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1dd3ff51bdfffa5fc48032ace31a2470')
sha256sums=('6705e8a252701bc162bbbe26f7cbb3e95e93a11af6288456ab711f5d0c0df929')

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
