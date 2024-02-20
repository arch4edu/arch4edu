# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=TeachingDemos
_pkgver=2.13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Demonstrations for Teaching and Learning"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Artistic-2.0')
depends=(
  r
)
optdepends=(
  r-ggplot2
  r-logspline
  r-png
  r-rgl
  r-sf
  r-spdata
  r-tcltk2
  r-tkrplot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('68f2977331442468df3080d365ce886a')
b2sums=('a6f005d891fdabb12d167efdbb22df2ddc41523db922ac380eb11f3c6cb2f336e0d35c0fa77dc198c197a4c1671b931e0b24241f4306124a447a27e8c6644770')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
