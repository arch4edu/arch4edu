# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=dimRed
_pkgver=0.2.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="A Framework for Dimensionality Reduction"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-drr
  r-magrittr
)
checkdepends=(
  python-tensorflow
  r-coranking
  r-diffusionmap
  r-fastica
  r-igraph
  r-keras
  r-pcal1
  r-rann
  r-reticulate
  r-rspectra
  r-rtsne
  r-tensorflow
  r-testthat
  r-umap
  r-vegan
)
optdepends=(
  r-cccd
  r-coranking
  r-diffusionmap
  r-energy
  r-fastica
  r-ggplot2
  r-igraph
  r-keras
  r-kernlab
  r-knitr
  r-loe
  r-nmf
  r-optimx
  r-pcal1
  r-pcapp
  r-rann
  r-reticulate
  r-rgl
  r-rspectra
  r-rtsne
  r-scales
  r-scatterplot3d
  r-tensorflow
  r-testthat
  r-tidyr
  r-tinytex
  r-umap
  r-vegan
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1cef3b06c7f0eea422fedbbf04a28e63')
b2sums=('e68bf03cae0c60703b7952a3354ea29fbd28a6594903c2fc0188f9aefe619b142dcde29a7eaa44c003dbf701fd0f302a49f13392781e73a3ca50d78379f48a81')

prepare() {
  # fix import in test
  sed -i 's/requireNamespace("FastICA"/requireNamespace("fastICA"/' "$_pkgname/tests/testthat/test_fastICA.R"
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
