# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=randtoolbox
_pkgver=2.0.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Toolbox for Pseudo and Quasi Random Number Generation and Random Generator Tests"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r-rngwell
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a17ceb0e2e5062191249235e50e832f6')
b2sums=('e2b0b762355e56c03c9312395651a8cb8616243596b16740cf3695e8f5c6bfc842abcf3097c9eba78ade616f6c829c8b631b8c3c484c43314f332bf0d8221cc7')

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
