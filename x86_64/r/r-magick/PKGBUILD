# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=magick
_pkgver=2.9.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Advanced Graphics and Image-Processing in R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  imagemagick
  r-curl
  r-magrittr
  r-rcpp
)
optdepends=(
  r-av
  r-gapminder
  r-ggplot2
  r-gifski
  r-irdisplay
  r-jsonlite
  r-knitr
  r-pdftools
  r-rmarkdown
  r-rsvg
  r-spelling
  r-tesseract
  r-webp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('012ecba2c6bffc0d79f56658b3cb808c')
b2sums=('5e2ec003dcec6e44c918853e5162d9ffbb5eafb194dc2075ab4e1b1c1e90a34a10565d51fd992e86efd04a9112584f9fd09c8b7ee8328b26b59221fd0efc4645')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla encoding.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
