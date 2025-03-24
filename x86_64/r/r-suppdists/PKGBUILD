# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=SuppDists
_pkgver=1.1-9.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Supplementary Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-rcppziggurat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f1a8585c9511b9d93788cf38b8207c48')
b2sums=('e1a3e57a1f7b26b7ce369e53a11d11a7b9935f6cb5affbca1cab74288729223245c3a6cecc7aa7a366b919b1cb228e38f3d35c31a25274651ba656f8cb80c26e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
