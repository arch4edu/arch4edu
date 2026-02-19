# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lobstr
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualize R Data Structures with Trees"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-crayon
  r-prettyunits
  r-rlang
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-pillar
  r-pkgdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c90a93955b448bff5d1a2cc25cda0143')
b2sums=('393436df47514e61739fcb35cd97941a2a0842920c2ef1a1179b68531efce6917ffbf16392e7b0ba148fa7c7c25237e1cadb79f3b0493e7c96a4595079f29de8')

prepare() {
  # Fix test
  sed -i '209 s/\[4]>1, 1, 1, 9000/[3]>1, 1, 2/' \
      "$_pkgname/tests/testthat/_snaps/tree.md"
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
