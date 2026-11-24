# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjags
_pkgver=5-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Graphical Models using MCMC"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  jags
  r-coda
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('14406a1ba4c0d3af38eff48c393fa25c')
b2sums=('f40d71b56e309abf104930e2e3f55a408f34743c7a7c17ab11dc9c981a521330a0859e42973b97aa47a3b83113ba8c46665070f4d6e62cf8d510d252340cfaaf')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
