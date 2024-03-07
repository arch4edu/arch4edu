# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LiblineaR
_pkgver=2.10-23
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Linear Predictive Models Based on the LIBLINEAR C/C++ Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-sparsem
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d273f6ac41fba1e7a32e3938f26c433d')
b2sums=('542ff72cbb7a706b3e16eac41617da2a5e425c551bbe77fd14c981d952bc14d857e1997c171b277c002997617425859d2b21756446c24f560e97d0fd15bf4061')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
