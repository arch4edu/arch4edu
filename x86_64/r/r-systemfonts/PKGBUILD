# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=systemfonts
_pkgver=1.3.4
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
md5sums=('46aabda9e6a407fc69582746c9d389a1')
b2sums=('e7df0c79965668336979ba8658f396c818d22b2e9a0ce27cb53fa25d98622c646fbf11be8d0d019be0f824cd81e56a5fa054f7df4291c853aad5825be94432fd')

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
