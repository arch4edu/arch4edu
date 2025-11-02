# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=listenv
_pkgver=0.10.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Environments Behaving (Almost) as Lists"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r
)
optdepends=(
  r-markdown
  r-r.rsp
  r-r.utils
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9bdcc598c6f0465ef80021c72cadeede')
b2sums=('567e6919c1321140c792cf0f8138259aa2ffa863f8a4156c02518a3e64feb29ca4487db466d6342b92fe698d04cf18493b039e6d93614de2daae471b1c68ab7e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
