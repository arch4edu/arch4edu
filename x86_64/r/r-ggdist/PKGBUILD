# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggdist
_pkgver=3.3.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualizations of Distributions and Uncertainty"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-cli
  r-distributional
  r-ggplot2
  r-glue
  r-gtable
  r-numderiv
  r-quadprog
  r-rcpp
  r-rlang
  r-scales
  r-tibble
  r-vctrs
  r-withr
)
checkdepends=(
  r-beeswarm
  r-fda
  r-fontquiver
  r-mvtnorm
  r-posterior
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
  r-dplyr
  r-fda
  r-fontquiver
  r-knitr
  r-mvtnorm
  r-patchwork
  r-pkgdown
  r-posterior
  r-ragg
  r-rmarkdown
  r-showtext
  r-svglite
  r-sysfonts
  r-testthat
  r-tidyr
  r-tidyselect
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a86ba0cdc1040b4a5f2331b38b9c27fb')
b2sums=('2bc1fefe3f723d73c5555f3be57bd1c75b1d96a0dfd86e56b10fbaa4f1525cc2973b432bce82bbdc93f7057e2d63b52b3f1cc78e3a770feee13846ea70800b86')

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
}
