# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=diffusionMap
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Diffusion Map"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-igraph
  r-scatterplot3d
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9f9f0fa8861d315c9bedacac394831b6')
b2sums=('6c0193db73bf2d5f2a21bb72d486c3888ad988936b066c3ea69c424db8b74027a37f480b71a3e2d8db1ba14f77eecf9c3e7f2fedba27bd26c1c6ba1637ec92bc')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
