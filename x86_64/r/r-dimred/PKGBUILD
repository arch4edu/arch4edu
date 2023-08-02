# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=dimRed
_pkgver=0.2.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="A Framework for Dimensionality Reduction"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
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
sha256sums=('9a7eb14781f01a12e26e7b26a91c8edaca7d824b9c1ffe74c81837098d9bf417')

prepare() {
  # fix import in test
  sed -i 's/requireNamespace("FastICA"/requireNamespace("fastICA"/' "$_pkgname/tests/testthat/test_fastICA.R"
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
