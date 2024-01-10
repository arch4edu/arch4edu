# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=BH
_pkgver=1.84.0-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Boost C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(Boost)
depends=(
  boost
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('34c6a9cf6213e6e93417b3168c4c84b4')
b2sums=('3747e6ad5c8534abf9ca54159002628fbfdd9adec9ed28cee4e38a5e6a96e2605ce1ed63928c26e04abcd81d3df592b5fcde4281762407aad98ecdca350ac873')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  # Use system boost headers from the `boost` package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/include"
  rm -r boost
  ln -s /usr/include/boost
}
