# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=rappdirs
_pkgver=0.3.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=13
pkgdesc="Application Directories: Determine Where to Save Data, Caches, and Logs"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
checkdepends=(
  r-testthat
  r-withr
)
optdepends=(
  r-covr
  r-roxygen2
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('cafdd5478c4a6094a9f3d7335fb4f889'
         '86106366bdf6586bb505dcc53dcc1ba2')
b2sums=('2dd360804783d56269f4f9c96cfe057ba431ee9d71e69227f2338feec06cbff555d1707e01a2830647a7d7421d7dbc56452b88b985971cf1feb5d21bc1452cea'
        'a8b98e83b9cafdf1117627c99c13ec5fb2b05176d8c031e07eb888230e23d3a280308d8012c0dbf0312b22f83eca522f249155dfef0d8dd4855b4a7512e6d3e5')

prepare() {
  # fix outdated snapshot tests
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
