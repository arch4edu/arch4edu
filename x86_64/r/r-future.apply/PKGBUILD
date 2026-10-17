# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=future.apply
_pkgver=1.21.0
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
md5sums=('4aae6b7e660b430da06a5df549a2fc5c')
b2sums=('ddecaf56bcffdb022f66846e916f4b9f1c86fbb963b1fd31678582b6de4606944749909a5e8bd1124a963e2e56ab8cd7907711b51f49c4d48643d3aeb77bb6b1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
