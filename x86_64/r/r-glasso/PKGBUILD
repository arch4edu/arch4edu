# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glasso
_pkgver=1.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Graphical Lasso: Estimation of Gaussian Graphical Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL2)
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f0b42c09df8d4845624821cb2d017f45')
b2sums=('b40c3bb46da06349b5b41abe55cbe756ce57a666d2abebd03d758576f5882496b99c9a3e4fd0a8b55ea2636eff1fac6ac227b096f3842c2b7f29f31935ac7efb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
