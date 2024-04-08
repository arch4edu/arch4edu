# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=daewr
_pkgver=1.2-11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Design and Analysis of Experiments with R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-stringi
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ed0ec58f19b45350ee2ac53af0b4ecff')
b2sums=('9486a72e1797b8d30fb3c07a68411b1385627a488cfe6deb075d7d28e2faa3b2fb93ab2aefe74ee91738acb7c67fc34512ecaa0d473877f56ab3391906a390dd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
