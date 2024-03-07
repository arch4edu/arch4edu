# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=AcceptanceSampling
_pkgver=1.0-10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Creation and Evaluation of Acceptance Sampling Plans"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cccf037fcede6abc4636d6d4cfe88d0f')
b2sums=('ee6e7b5a2fd116c1cd0be0ec04ea009cf05677a1e1ec8bc70516b4da2732cdf32502a70b5d4f5df8fd59fa9dbbd1f941fa1b6011edd2cecdc5a53bc477529268')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
