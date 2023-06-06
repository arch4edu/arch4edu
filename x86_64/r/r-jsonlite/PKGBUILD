# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=jsonlite
_pkgver=1.8.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=5
pkgdesc="A Simple and Robust JSON Parser and Generator for R"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r
)
optdepends=(
  r-httr
  r-knitr
  r-r.rsp
  r-rmarkdown
  r-sf
  r-testthat
  r-vctrs
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6c49fda00ace69deda82998c0b97427d')
sha256sums=('dc3cca4bdca1b6d6836c412760ea9656140683126c54cb89c3e42219dec4a3ad')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
