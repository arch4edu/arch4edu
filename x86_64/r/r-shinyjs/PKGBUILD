# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=shinyjs
_pkgver=2.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Easily Improve the User Experience of Your Shiny Apps in Seconds"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-digest
  r-jsonlite
  r-shiny
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-htmltools
  r-knitr
  r-rmarkdown
  r-shinyace
  r-shinydisconnect
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e7e6dcd145801997c1340f9d0e5f98af')
b2sums=('54524d77df47b7f9fa8dcdea71732a871aa91ccdd0d9c624cf7432dc7a60d7ff15eeadec32f97878774a36ec752b8c2fed9028b6b03662e91655cd2bfe360624')

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
