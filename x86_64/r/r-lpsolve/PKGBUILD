# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lpSolve
_pkgver=5.6.21
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
md5sums=('57d3e1be9f6e26555a2d77444a0ec79b'
         'cd8dd2b63a8ba9697c3c4a5569c7c9c5')
b2sums=('63e0665da09c978014695879c60ad5b7380c54e3267227309faedc47e290a8d206372ccbd98ba4727ba9bf32102f5cc7352b823b53ad8a8202bedf6a3ebae8bc'
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
