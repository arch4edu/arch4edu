# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sandwich
_pkgver=3.1-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('a5abc91469c1f1ae604dba272268b10b')
b2sums=('6d4ae6329c77573e4b1c7404746c3e1a8014b725fac58fd4bd84ebfa1f884b30e6a11056e318b28886dc504457200569ac77667a50b0a20cd1a51ffb4ae9198f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
