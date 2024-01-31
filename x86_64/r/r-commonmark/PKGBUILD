# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=commonmark
_pkgver=1.9.1
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
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-cmark-gfm.patch")
md5sums=('c95e6412ef2937d110128f35fd85be78'
         '31357c9e94c77a617485e752ead93868')
b2sums=('0e419756209153ce68a7a24d3c71230238f803b92396464324e83bbddbd90f354b220afd9e33ebe2e1fee9dcb4c860084b96a523e68d6ae9e4062d73501eb0ee'
        '02fda554b3d786bab69b214e1281da56968dc943cd1ebda829576b6858e2c6167b2415f878c66bb7f6091d3581636d0135e8cd2f5afba99f9141c07aacbba686')

prepare() {
  # build against system cmark-gfm
  patch -Np1 -i system-cmark-gfm.patch
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
