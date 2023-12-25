# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributorr: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=modeltools
_pkgver=0.2-23
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=12
pkgdesc="Tools and Classes for Statistical Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL2)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('954e3f72a5fd9086f070f7fcc41a08f1')
b2sums=('af734abbab0177159bcb62babe233d777c697d510d0d152b3b1303c02e174a2ee6bc1a3767725ba89b20a83222a1e848d62ac31cf625d0ccc0aa3db150204c33')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
