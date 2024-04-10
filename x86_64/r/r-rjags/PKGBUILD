# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjags
_pkgver=4-15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Bayesian Graphical Models using MCMC"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  jags
  r-coda
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7c8e06d355256b595dc94cc47385a0f0')
b2sums=('bae7bf5b445fc3d8c525cceb0b6544ea4f68c53e462c27a1a9e58033a95ef20cb2317e8628ea9f77b05136c3df0943a8d4d5bd8cbd501a09dbd9b6de77371ed2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
