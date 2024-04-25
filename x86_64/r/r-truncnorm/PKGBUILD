# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=truncnorm
_pkgver=1.0-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Truncated Normal Distribution"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('878c944c50c6eeaea3e4e6d9586216d3')
b2sums=('62a51ed8e4e03ad7e39d0782365ae70861c20368c36466b78af7e5a1fe00a048275866497e9b1ec04b5e01ae0ffa4bdae7d8fc93779f646c135cf68800236fa3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
