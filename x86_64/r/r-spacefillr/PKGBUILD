# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=spacefillr
_pkgver=0.3.3
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
md5sums=('00ba85c2e07532c40537458098843297')
b2sums=('fa703c6cf9c18c1182de5eec0a7972affc5d3bec06ef3295126aa6d7614d3fd952a0165b127a53334fa84c45646def536b7a44ad8cf3c52cb474c542aa398bf3')

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
