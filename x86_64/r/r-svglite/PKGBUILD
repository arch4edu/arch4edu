# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=svglite
_pkgver=2.1.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="An 'SVG' Graphics Device"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  libpng
  r-systemfonts
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-fontquiver
  r-testthat
  r-xml2
  ttf-liberation
)
optdepends=(
  r-covr
  r-fontquiver
  r-htmltools
  r-knitr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('46154cf187ad6ec377269b6307de16f4')
b2sums=('6a2a1dc2a4e08bc7e93a7ddc9ce9a8e0451974bb186ab88351603a6cd5d69cb5a8f71c0087be288e935fd2d3cf7515f67a9bea4f2c545132f1c7a2249a5af8c9')

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
