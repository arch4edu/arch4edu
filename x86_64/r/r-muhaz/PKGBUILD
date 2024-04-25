# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=muhaz
_pkgver=1.2.6.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Hazard Function Estimation in Survival Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6021d80354ee966f0d7be4ba6ce8c2d1')
b2sums=('f724117788269e53de36c1e4790914185998caf417925dffa7225d7c42afba6a928d5690643ccdd6d430d36883d42ac6fc3a683757018ee27abe480c80723e49')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
