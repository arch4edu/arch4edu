# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lpSolve
_pkgver=5.6.18
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
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
md5sums=('ad4e2a89dc675be45e2ed24f9a00d831'
         'cd8dd2b63a8ba9697c3c4a5569c7c9c5')
sha256sums=('751e1926fcd81b852b6c0d5ea7ecd9311ef6fbdbce9143b7872fea79590de712'
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
