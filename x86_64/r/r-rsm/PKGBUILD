# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rsm
_pkgver=2.10.6
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
  r-vdg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c5f99674b83826141adaebbefe9060e6')
b2sums=('2b377aa1270f33c24fde54167e0e2378f6689140383f74f90a6d79e803cc581e3d13be6b452174d2205a849fced23febbfb6c5f32564a05cfc0bc72b89f618e0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
