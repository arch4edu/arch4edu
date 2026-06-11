# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=filelock
_pkgver=1.0.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Portable File Locking"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-callr
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('db8ce0e4e54049a51875108aa996bbdb')
b2sums=('c36a82cc7c4f0720e84b400b3c800c0719ed1a526ea41ec9cad06c00371b5058ad5b08478c2da67b649bdee1acfeab2aaf51f1abb01b55ca639863bc8104aee0')

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
