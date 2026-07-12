# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sandwich
_pkgver=3.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Robust Covariance Matrix Estimators"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-zoo
)
optdepends=(
  r-aer
  r-car
  r-geepack
  r-lme4
  r-lmtest
  r-multiwayvcov
  r-pcse
  r-plm
  r-pscl
  r-scatterplot3d
  r-strucchange
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('78726157af8e9936d1c2918158bf8530')
b2sums=('55c3fcfc5cfceb8b1c7c0b44aed86d7405c1c32a089d04b1e1d236c0ffdacfd4346ee7b256b92a4031ad8c906276a0131241e8bc371d4df09c3fbe1f63ca870d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
