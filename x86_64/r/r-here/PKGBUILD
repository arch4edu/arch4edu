# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=here
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="A Simpler Way to Find Your Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rprojroot
)
optdepends=(
  r-conflicted
  r-covr
  r-fs
  r-knitr
  r-palmerpenguins
  r-plyr
  r-readr
  r-rlang
  r-rmarkdown
  r-testthat
  r-uuid
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('67367162e286ae95c06abb6e7d70dd75')
b2sums=('840269e8beaf58ef987bdb54fe51110e39d3e071da0623cb9b687d752b80714837a415fdf7618b1c6fa02fe8f5facd0aa700e82d34f6d2ca4579294af410ac71')

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
