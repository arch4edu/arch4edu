# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=commonmark
_pkgver=1.9.2
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
md5sums=('02c2b4ba170610b672092708a39fa479'
         '31357c9e94c77a617485e752ead93868')
b2sums=('b9ffda0e5413cc60b66be37a547dba956b1c2883b4cb99ae4dc03b99f881fe4535568dd052322c97983784fd3cf0ae669e43e501c429d5156c84dc92206f3b6e'
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
