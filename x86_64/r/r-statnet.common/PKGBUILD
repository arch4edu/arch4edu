# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statnet.common
_pkgver=4.10.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Common R Scripts and Utilities Used by the Statnet Project Software"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-coda
)
optdepends=(
  r-covr
  r-rlang
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('debc899fef50b20c86c995966244ad30')
b2sums=('20b013b408c79fe31e85be8877319ad6e622455187e60b2692f2e8319dd40ed10b46f6d89883bbfd3d61ca4fa048386fd1e3c522cd979018a98379f42598d3fb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
