# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=TH.data
_pkgver=1.1-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="TH's Data Archive"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-atr
  r-coin
  r-colorspace
  r-dplyr
  r-gridextra
  r-knitr
  r-multcomp
  r-openxlsx
  r-plyr
  r-rms
  r-tram
  r-trtf
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('399d57a67a697c40c74a86db3678ae8a')
b2sums=('4e94a9c525cdcdbc2339edd6c91e08e6bb847f706ce562e9bd8269e4795bdf9d1d4fdd27d86e4cc0e8433c724a291a1fd88967a7f8b01dee0fc58a50a7e215df')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
