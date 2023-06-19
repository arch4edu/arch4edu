# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=BH
_pkgver=1.81.0-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=3
pkgdesc="Boost C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(Boost)
depends=(
  boost
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('897f0d1cd97ba1047eff09acf68c07a8')
sha256sums=('f51c8badd6f181e06353314e1d15a6ec1495cc498ee74b6fa4ea8aba6e97ff64')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  # Use system boost headers from the `boost` package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/include"
  rm -r boost
  ln -s /usr/include/boost
}
