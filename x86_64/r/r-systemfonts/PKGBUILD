# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=systemfonts
_pkgver=1.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="System Native Font Finding"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  fontconfig
  freetype2
  r-jsonlite
  r-lifecycle
  r-base64enc
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
  ttf-font
)
optdepends=(
  r-covr
  r-farver
  r-knitr
  r-rmarkdown
  r-testthat
  r-ggplot2
  r-ragg
  r-svglite

)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('670a7c3c036e1fe49af2d5fb10469405')
b2sums=('1d5a86fd9fafcc86d73951d2d29a1eb3d649362aa4cd36034972f9fcf0085bbfaf08227718b06a4c8880c8d83d51db781e093e0d014590c11744f7097d81239d')

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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
