# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=admisc
_pkgver=0.40
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Adrian Dusa's Miscellaneous"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-qca
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('dc4da9b9d0db73a758e0a05a43d6f60f')
b2sums=('e2c610d899ec0ea676ce0d364b31534a23ceaa64999afaa879955ee025d75932fe53483d04a6d3271292323e0271c80337aede16ec8abded1635c0f9c73c0458')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
