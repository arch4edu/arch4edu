# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lobstr
_pkgver=1.2.2
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
md5sums=('571ea0c261b5d28cd033e1dd43d44b00')
b2sums=('84237bf6ecfab1dea0a8ee33b7b9eb14a0a82ebeb858ed69f0e5423d2bf60323e6b07b4074847a6d9d027b0f3ba300a62c137f3fb7fa0177193cf088da84d99f')

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
