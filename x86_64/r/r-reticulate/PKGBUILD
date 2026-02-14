# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=reticulate
_pkgver=1.45.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface to 'Python'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
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
  "ipython: IPython console app"
  "python-numpy: translation between R matrices and NumPy arrays"
  r-callr
  r-cli
  r-glue
  r-knitr
  r-pillar
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('21fe23c10ea76e13fbe076fcd10a272e')
b2sums=('8055fb96ed01b3b3de420be1b804d8de848f9619f410af733a0e536259e8921ba1dfca5a922180b6cb1a68aeeaf1d5f7b431570590bb11dbe07c6304bc313505')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"

  # compile python bytecode
  python -m compileall -o 0 -o 1 -s build -p /usr/lib/R/library "build/$_pkgname/python/rpytools"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
