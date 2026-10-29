# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=poorman
_pkgver=0.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Poor Man's Dependency Free Recreation of 'dplyr'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-roxygen2
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bd99f902813e557c9412b19fa6ef073f')
b2sums=('c863709bfeb66d66a2a795bd031a60f58bab190048231ca69b92b9df3c55f2335ed6efe17f790b62f70c973a9fead51133e9f5765512a5a31d534819821af2b4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
