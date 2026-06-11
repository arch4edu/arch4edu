# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=BH
_pkgver=1.90.0-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Boost C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSL-1.0')
depends=(
  boost
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4b82aea7c6223ea0048c3edbe1a2caa0')
b2sums=('88ecd04248d5e765efc5529b075c9a66c3c2c7530ebcc56ed6abaa687fd204c218945d588cf126dbcceeaaaa952e9a47f58e30c77fed1925e97d608aaec17d54')

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
