# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: anzi2001 <anzi2001 at gmail dot com>
# Contributor: haha662 <haha662 at outlook dot com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=tinytex
_pkgver=0.50
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Helper Functions to Install and Maintain TeX Live, and Compile LaTeX Documents"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-xfun
)
checkdepends=(
  r-testit
)
optdepends=(
  r-rstudioapi
  r-testit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d82bbbf55cbc746ca1ba74fedf9ee27b')
b2sums=('00afc360d41659035052a143889ed69d34bac22f13e3cf924b29638ad5f49f098e5bbb689d7b95534f4e6964061e27883f39da07bcff8b3328dce32f8f8666ed')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-cran.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
