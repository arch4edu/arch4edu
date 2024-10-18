# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=randtoolbox
_pkgver=2.0.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Toolbox for Pseudo and Quasi Random Number Generation and Random Generator Tests"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r-rngwell
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95a10075ea0c91f485545c876356d78b')
b2sums=('243d541b5f084d23a36844a55b1e8b97d4e342a5542fc673e758464121687ea8d9cf764d4b2c5539c81058e6154ba9fb79a78f658904db6396ed05a5f9cd06d0')

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
