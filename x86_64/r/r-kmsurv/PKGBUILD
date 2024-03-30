# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=KMsurv
_pkgver=0.1-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Data sets from Klein and Moeschberger (1997), Survival Analysis"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4979464e3ee73b03891b66e53231b2be')
b2sums=('40ea4df71463513ae2aaca03bf415cc00a349f68eaba23363afad3dc89d4f423197bf293256ba936c7e20a3ae40bb721320780629c959a4d0cbafc38b91968e7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
