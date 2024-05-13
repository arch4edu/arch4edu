# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=estimability
_pkgver=1.5.1
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
md5sums=('90c2834919962894b19fa023eed3072e')
b2sums=('650c48287112b71922f603653b3f77107a8e1be1f5a671f7ad1cc80440096885be7f58eb3a3484a5668718ce8fd327bffc0eba7082850aecb611b9e3f24d76c2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
