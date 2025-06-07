# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=future.apply
_pkgver=1.20.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Apply Function to Elements in Parallel using Futures"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-future
  r-globals
)
optdepends=(
  r-listenv
  r-markdown
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('49fbb87784f16d304d136a4e469deaf0')
b2sums=('cfc47bda8b14501e296e0d03f9ab9df54111f6f045fa3316e1207a66cdf7010dcbf89839b9f026d8aced98d407fa268058ed70a17acd03139ca6ef08e4a91522')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
