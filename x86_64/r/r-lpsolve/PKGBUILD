# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lpSolve
_pkgver=5.6.20
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('82005adb4666e53da367a88885842a17'
         'cd8dd2b63a8ba9697c3c4a5569c7c9c5')
b2sums=('ca55ec356519debaffd85894e4a2d80abe42dc8adaceaa43578ab2825eae8d45044117244e72be6989b4e166c8d06dc66b691e2f628e771c741c16491159ee5a'
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
