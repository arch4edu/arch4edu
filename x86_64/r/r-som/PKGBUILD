# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=som
_pkgver=0.3-5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Self-Organizing Map"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ab2dcc4529c70d4b5f223a22d23a4d4e')
b2sums=('e69a6c78708eaf3b4b4d9672199fe763c50e46b6dc13faa12653693665c1af65916618c23b8e1823cff905d32ee34a582973b070ad409a78c3fa86c28586849f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
