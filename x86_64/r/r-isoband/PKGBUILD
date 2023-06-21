# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=isoband
_pkgver=0.2.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=3
pkgdesc="Generate Isolines and Isobands from Regularly Spaced Elevation Grids"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-ggplot2
  r-knitr
  r-magick
  r-microbenchmark
  r-rmarkdown
  r-sf
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7241f95bafb46b44aa380b9a71b10467')
sha256sums=('7693223343b45b86de2b5b638ff148f0dafa6d7b1237e822c5272902f79cdf61')

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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
