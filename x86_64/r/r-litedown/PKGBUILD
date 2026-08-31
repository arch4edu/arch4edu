# Maintainer: Guoyi <kuoi@bioarchlinux.org>

_pkgname=litedown
_pkgver=0.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc="A Lightweight Version of R Markdown"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r-commonmark
  r-xfun
)
optdepends=(
  r-rbibutils
  r-rstudioapi
  r-testit
  r-tinyimg
  r-tinytex
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f1faa1676570c7c4a4dad09b4d0986e9')
b2sums=('776798bc2a524145a04bdacc602496bc517333adf9f33ec7917abec291c8cb51c1a49329331b07e14e9bedb3d528264e64351f52cb22bbeb9d698058c134c96a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
