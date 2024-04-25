# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=foreach
_pkgver=1.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Provides Foreach Looping Construct"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
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
b2sums=('90d4d2e06bd979055acc52c2697581648b10e837ff6cc8b353a550c774ca95262f4da9708fc7beb764c78073968b1c69fa7d43571c826f81403a31f936dadfb3'
        'ab10768e502e84fd50e4afcf89fa4867f994f9c9f9371d0b591b92e030d17d3d8a3075ccb87da66ac6b57c86b20197485b7d823acc074964ec1d1d9eaa8690b0')

prepare() {
  # skip parallel tests in order to avoid a checkdependency on r-doparallel
  # which would cause a dependency cycle
  patch -Np1 -i skip-parallel-tests.patch
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
}
