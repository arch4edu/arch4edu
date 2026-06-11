# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=alabama
_pkgver=2025.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Constrained Nonlinear Optimization"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0a84d6bc753a287767dac4b354a8eef3')
b2sums=('9a5110ef742056af9dae4f562d1da431e05b5b569b8b9476fbfb9e4f0de40e274411a6d7afdd18f06fd73b258aca0c560c670bf8006b8df6a5d902f6bdf915db')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
