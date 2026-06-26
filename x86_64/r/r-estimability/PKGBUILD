# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=estimability
_pkgver=2.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Assessing Estimability of Linear Predictions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a3060510843713ed688963c36d09b441')
b2sums=('b00b403f9186109fac6b817f7bb49902f22c5b0d573cf7b0ea24f94e9dcd7a2a069206d9a52353f65bc1e5376b53eeb174878d4a3f2a20f5856658559ea6561f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
