# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=commonmark
_pkgver=1.9.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="High Performance CommonMark and Github Markdown Rendering in R"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(BSD)
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
md5sums=('a6c6a1c1bf0ee0cc0cde65ce2d577cfc'
         '31357c9e94c77a617485e752ead93868')
sha256sums=('6dd01a5a26c8d436486abf69c2f6ad0f8dd1c811f575c31983aeb4dbd376548f'
            'd2360beb79eeee5fcb34e468704aa9af1c98c6effbe2cadafde4f32a6d6fab86')

prepare() {
  # build against system cmark-gfm
  patch -Np1 -i system-cmark-gfm.patch
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
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
