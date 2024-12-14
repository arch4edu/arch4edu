# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lpSolve
_pkgver=5.6.23
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface to 'Lp_solve' v. 5.5 to Solve Linear/Integer Programs"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.0-only')
depends=(
  lpsolve
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-lpsolve.patch")
md5sums=('163acadfcb3c04eb0889bc6e13484ca4'
         'cd8dd2b63a8ba9697c3c4a5569c7c9c5')
b2sums=('35cf71c7a802ea497fe7db72f1cca493636af532607ae1c4f71b4111c04266aced56d1b23ea947008088fc801a8c9eae63002cc41208874347aebec09b0af5ff'
        '769a1dd7a495e778484785980b19c4558c9c82ec9b812ff13e40a0745f631af109a143e7613aad53dbaf70936fb02a2401e4f50675bb48d5b1155c391cedabc4')

prepare() {
  # build against system lpsolve
  patch -Np1 -i system-lpsolve.patch
  rm "$_pkgname"/src/*.h
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
