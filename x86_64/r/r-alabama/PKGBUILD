# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=alabama
_pkgver=2023.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Constrained Nonlinear Optimization"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c5c8ed8a90efc7e142140f30237f4de6')
b2sums=('dc58536ab06ffc21d7514d8e27d08ce17e53d27654e44897a3692b75cc4a2982c6efe3def516dcd06f29838bc8e8188982a78bec0543df8301ba1ea83886b36e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
