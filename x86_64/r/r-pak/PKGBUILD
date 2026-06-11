# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=pak
_pkgver=0.9.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Another Approach to Package Installation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-callr
  r-cli
  r-curl
  r-desc
  r-filelock
  r-jsonlite
  r-lpsolve
  r-pkgbuild
  r-pkgcache
  r-pkgdepends
  r-pkgsearch
  r-processx
  r-ps
  r-r6
  r-zip
  r-keyring
  r-yaml
)
checkdepends=(
  r-mockery
  r-testthat
)
optdepends=(
  r-covr
  r-gitcreds
  r-glue
  r-pingr
  r-pkgload
  r-rstudioapi
  r-testthat
  r-withr
  r-webfakes

)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libs.patch")
md5sums=('dcedd9fca4f9603fc2793ea2686dc2c9'
         '29b1470e2d25f82ebeafc02fe3b2594a')
b2sums=('ef89e33cb8f40b1b80c049c602122c66a46ce2c7e2ad4075d41b85863ee0aebf9cecd55943098e20b98fede494ff416a959dffccaa0a36a719d5e840978c0719'
        'b422c6a23d6850831433fdcf3e81684189bdaea1735fcc85edeff3202fe084f4167876949ff9ddfd5654cb2ce202ed005800a217dfe9bb12fb8240456880b4f1')

prepare() {
  # devendor R dependencies
  patch -Np1 -i system-libs.patch
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
