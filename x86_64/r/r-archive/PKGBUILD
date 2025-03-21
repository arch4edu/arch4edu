# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=archive
_pkgver=1.1.12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multi-Format Archive and Compression Support"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  libarchive
  r-cli
  r-glue
  r-rlang
  r-tibble
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6c1c04f13dd44befb57748d36d7a3685')
b2sums=('2415bbc12f7d9a8941da07aca1c2bbd54b6f4e66bfbcad8cced3378824f64e039b03f99d3d6b2f4b84b9fafc45928d34fe9b3bbb77d3158d3812bc82239ba7fc')

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
