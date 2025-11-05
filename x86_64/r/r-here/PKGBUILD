# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=here
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('d2ff22b1f33c99b75ab3597ef0f79506')
b2sums=('7005d20fa70c415a26c626d410b6954ee28e707754401a5a4594d87385b53e50c6896d287a81e046a6ace3bbfabdc23941ea1842e4d9842d74f69763839dc0f2')

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
