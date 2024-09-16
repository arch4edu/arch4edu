# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sandwich
_pkgver=3.1-1
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
md5sums=('fe33d8ee7c66fddae484817ca295f405')
b2sums=('510fc6c4acae4abc6701bb0af782696cc91e9ffea98f571f3da96e6305d2e58e7bebde88dd2cb3a0a20b840812d7429dac704034834fe0f0915f513ea2e074e3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
