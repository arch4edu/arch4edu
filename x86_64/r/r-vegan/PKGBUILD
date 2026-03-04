# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vegan
_pkgver=2.7-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Community Ecology Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-permute
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-knitr
  r-markdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1fb5c68eec22982f3ebb11dedf97448c')
b2sums=('74421c9542bd93394d118614e441d9663461cda7665808fdaea343ad89c437ae544b30cf3a9529e9436e499945315ddc216c4de77faa42724232b1b77e0a8811')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
