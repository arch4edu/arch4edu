# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mle.tools
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Expected/Observed Fisher Information and Bias-Corrected Maximum Likelihood Estimate(s)"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-fitdistrplus
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ea907b283c4a37a3734f04e389780b32')
b2sums=('9624f979da3262a259fe5034a93184378e3e820f9ae61d83d9094025f07632539ebb43533b5d8dd6d41fb9502cb21933a0c5a4be6e891b658812960101bc5809')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
