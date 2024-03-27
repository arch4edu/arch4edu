# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=future
_pkgver=1.33.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Unified Parallel and Distributed Processing in R for Everyone"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r-digest
  r-globals
  r-listenv
  r-parallelly
)
optdepends=(
  r-markdown
  r-r.rsp
  r-rhpcblasctl
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5f66cf78cb629367c2c168c744181257')
b2sums=('e6cf59076920088bb9f134409fe3200d24b1d13c4a5c1b4716a11e2788ce8b84e4c0b937dff353196db16700e40b09072f86590ebdcbfd0d49fb3de4e7e0ae56')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
