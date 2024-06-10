# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rsm
_pkgver=2.10.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Response-Surface Analysis"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-estimability
)
optdepends=(
  r-conf.design
  r-doe.base
  r-emmeans
  r-frf2
  r-knitr
  r-rmarkdown
  r-vdgraph
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c26179c5a99162725a61d331087ace45')
b2sums=('08a976dcc3e535c842b13227d3c1e54162a5dbc32e336aadab530f64261c2d688fdf5e8e4a2b62fd835b54410234baa13c088a3d54e6ef297a03147e47c7c5ef')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
