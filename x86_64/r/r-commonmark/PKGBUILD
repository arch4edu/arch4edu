# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=commonmark
_pkgver=1.9.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="High Performance CommonMark and Github Markdown Rendering in R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-2-Clause')
depends=(
  cmark-gfm
  r
)
checkdepends=(
  r-testthat
  r-xml2
)
optdepends=(
  r-curl
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2a3cb69608d0cd2644fd857555305c86')
b2sums=('c5f389e30d1f35a224a85ba35671596ab86200c96d23faf329459bbe912584d988217caa79623820fef6ecf5a4162fa519071448118dfd77ae52aef5b37e7028')

build() {
  mkdir -p build
  PKG_LIBS='-lcmark-gfm -lcmark-gfm-extensions' R CMD INSTALL -l build "$_pkgname"
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
