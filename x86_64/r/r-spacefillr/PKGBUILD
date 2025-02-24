# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=spacefillr
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Space-Filling Random and Quasi-Random Sequences"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rcpp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7a56b0a69abbc787013d4e77cbf4cad9')
b2sums=('564acbc3292e9b5cd96d2697a61e0f51cbf8642ad83b867ddf8fea348405acfd9bb01f2d8fb51e561e8b253f16f87445e2182a585a56631c435d3d00175031af')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
