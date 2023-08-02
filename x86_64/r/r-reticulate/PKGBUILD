# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=reticulate
_pkgver=1.30
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Interface to 'Python'"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(Apache)
depends=(
  python
  r-here
  r-jsonlite
  r-png
  r-rappdirs
  r-rcpp
  r-rcpptoml
  r-rlang
  r-withr
)
checkdepends=(
  ipython
  python-docutils
  python-matplotlib
  python-numpy
  python-pandas
  python-pipenv
  python-plotly
  python-poetry
  python-scipy
  python-tabulate
  python-wrapt
  r-rmarkdown
  r-testthat
)
optdepends=(
  r-callr
  r-cli
  r-glue
  r-knitr
  r-pillar
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "scipy-1.11.0-fixes.patch")
md5sums=('9063282d659c73afbf9bcaec50878eb7'
         '4247ebf82b55d3bebfdd2f5235d082a7')
sha256sums=('ee8f8a3a90fa49faf802c345a23e103d897e40dadc5ec75bfb13ce06576017df'
            '943a11211e86181987e726e76801383bef4a433a82d86e953733e14b4e4a796a')

prepare() {
  cd "$_pkgname"
  # Fix compatibility with python-scipy 1.11.0 and newer
  patch -Np1 -i ../scipy-1.11.0-fixes.patch
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
