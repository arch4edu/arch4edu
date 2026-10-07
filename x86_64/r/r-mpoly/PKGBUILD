# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=mpoly
_pkgver=1.1.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Symbolic computation and more with multivariate polynomials"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
  r-ggplot2
  r-orthopolynom
  r-partitions
  r-plyr
  r-polynom
  r-stringi
  r-stringr
  r-tidyr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('014212ffd04a0b8c637a0b3d23ceeed5')
b2sums=('c61b9e16762843f3c8ed8000c3c3565ca551667fecdb31e04152feb0c306860fe5287372006cd5fed8df5723dc03872f8ca848f632a3dc6bf0a788535a33c924')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
