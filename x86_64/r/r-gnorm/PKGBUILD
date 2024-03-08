# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=gnorm
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Generalized Normal/Exponential Power Distribution"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('77860053c6b31b281801e89977cd7a67')
b2sums=('fd97810423d86987b66022969008f1d3ec3f1d1e88c1b646e2eee012e095a3d931cbd4603fcd2f2e3dd22759ff94224af2748142f1428f919038969990bd8f89')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
