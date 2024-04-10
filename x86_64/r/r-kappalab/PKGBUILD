# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=kappalab
_pkgver=0.4-12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Non-Additive Measure and Integral Manipulation Functions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('CECILL-2.0')
depends=(
  r-kernlab
  r-lpsolve
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cd88e018c6513b3931021f2391c6282b')
b2sums=('59d191c1e249b4b5435b1c2fcf35b7805e8030eea85eb6cfc714b690ae421a688dbf1d63ae05a37f040bfb7efa80d19e030504344d21281583c539ed67ae1358')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 "$_pkgname/COPYING" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
