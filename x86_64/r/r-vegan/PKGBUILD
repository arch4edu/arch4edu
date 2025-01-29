# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vegan
_pkgver=2.6-10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Community Ecology Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-permute
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-knitr
  r-markdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('33763712c692f97b8d17cda1ab7793a0')
b2sums=('f1167d41dcbd715c60acea9b64e3a928a98f5d6c45f9b272cb1230e538ac1fd65625b4db41768e701a9b085bf8a6233bae7999e9b40366a7158da244aa946b98')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
