# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=admisc
_pkgver=0.39
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Adrian Dusa's Miscellaneous"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-qca
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b7ced0ecfe6f3e7291358e66c1214ca1')
b2sums=('e1ebd7775095e380951434c74543414e7ac44ecd8d777e408b840144ce9be569e966c84dc31775ff97093afb600eff89ce5729fcc186e0061a802de3e81bdcf3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
