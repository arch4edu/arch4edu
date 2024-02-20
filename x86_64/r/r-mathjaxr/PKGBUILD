# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=mathjaxr
_pkgver=1.6-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Using 'Mathjax' in Rd Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-js
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('aa2b8ff5e046b8681d3f0fdcdb046880')
b2sums=('39577dcf01ed3cfb3a00b40cbd7fb3c7597ed180974afc1842cc56f82136fe62e3ead8f93f7c92b3755573aa24c6c224887c48bfe145a99566e0ca6588f1faf3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
