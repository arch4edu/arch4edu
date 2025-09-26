# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=TH.data
_pkgver=1.1-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="TH's Data Archive"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-atr
  r-coin
  r-colorspace
  r-dplyr
  r-gridextra
  r-knitr
  r-multcomp
  r-openxlsx
  r-plyr
  r-rms
  r-tram
  r-trtf
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('14c93d658fe275e437416cff476bfa55')
b2sums=('895772447c7594443e72754401dc4158b13e4313ff5865db618f30282c25b0a01b8fa80449fc0870ba8b7b70ea57e707d276338e39934d9a5a294c429d990c5f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
