# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lpSolve
_pkgver=5.6.19
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface to 'Lp_solve' v. 5.5 to Solve Linear/Integer Programs"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(LGPL2.1)
depends=(
  lpsolve
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-lpsolve.patch")
md5sums=('695f93d25404d31a02a5aebe729d4d12'
         'cd8dd2b63a8ba9697c3c4a5569c7c9c5')
sha256sums=('49d5b49e64c6eba2bc4cea80eb615df21a2d0188b1bbffa05052dc978c94581b'
            '3e13cab8c42951ed332c1bcbcb20f9c0dd964e54007cd001051fbbc7828f0653')

prepare() {
  # build against system lpsolve
  patch -Np1 -i system-lpsolve.patch
  rm "$_pkgname"/src/*.h
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
