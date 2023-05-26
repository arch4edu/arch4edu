# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>

_cranname=Rcpp
_cranver=1.0.10
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Seamless R and C++ Integration"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r)
checkdepends=(r-tinytest)
optdepends=(
    r-tinytest
    r-inline
    r-rbenchmark
    r-pkgkitten
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('1e65e24a9981251ab5fc4f9fd65fe4eab4ba0255be3400a8c5abe20b62b5d546')

prepare() {
  # upstream issue https://github.com/RcppCore/Rcpp/issues/1251
  sed -i 's/-447.1974945/-447.197893678525/' "$_cranname/inst/tinytest/test_stats.R"
}

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" LC_ALL=C.UTF-8 RunAllRcppTests=yes Rscript --vanilla tinytest.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
