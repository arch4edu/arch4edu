# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=foreach
_pkgver=1.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=7
pkgdesc="Provides Foreach Looping Construct"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(Apache)
depends=(
  r-iterators
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-domc
  r-doparallel
  r-knitr
  r-randomforest
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "skip-parallel-tests.patch")
md5sums=('726beb5a50a3cec75261b4405158386c'
         '16b5d1acf5f3a8bdb699110a292278c3')
sha256sums=('56338d8753f9f68f262cf532fd8a6d0fe25a71a2ff0107f3ce378feb926bafe4'
            'e6a6de407c2fb1f926514b421cbea747d5e2b910bcb02664ed445dfb2779bc9c')

prepare() {
  # skip parallel tests in order to avoid a checkdependency on r-doparallel
  # which would cause a dependency cycle
  patch -Np1 -i skip-parallel-tests.patch
}

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
