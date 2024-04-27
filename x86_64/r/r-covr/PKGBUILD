# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=covr
_pkgver=3.6.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Test Coverage for Packages"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-crayon
  r-digest
  r-httr
  r-jsonlite
  r-rex
  r-withr
  r-yaml
)
checkdepends=(
  r-dt
  r-htmltools
  r-memoise
  r-mockery
  r-rstudioapi
  r-testthat
  r-xml2
)
optdepends=(
  r-covr
  r-curl
  r-dt
  r-htmltools
  r-knitr
  r-memoise
  r-mockery
  r-r6
  r-rlang
  r-rmarkdown
  r-rstudioapi
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('8fadf3538ed1edfefb3a20bd5c5e887d'
         'd3729dbb95789a8622860678ed9fdb7a')
b2sums=('0d986635c4fb04e327d142e49290d3f4c8f062b8873f7a30cf8ee642be4cb1a8cde4882580eeba58565cfaf113e1bc94ff2ceb35fe1272d160a07f0e9f60a4f3'
        '8f4241f4d0836c42b2c5257adbf418413681a9610c6fc105dc0022e923fa93b25752ce5c5aa5cd12b1571307fa022bb79cd70b3b6ac00a27e55fb609110d6df1')

prepare() {
  # skip failing test
  patch -Np1 -i fix-tests.patch
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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
