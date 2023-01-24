# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=BH
_cranver=1.81.0-1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Boost C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(Boost)
depends=(boost r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('f51c8badd6f181e06353314e1d15a6ec1495cc498ee74b6fa4ea8aba6e97ff64')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  # Use system boost headers from the `boost` package
  cd "${pkgdir}/usr/lib/R/library/${_cranname}/include"
  rm -r boost
  install -dm0755 "${pkgdir}/usr/include/boost"
  ln -s /usr/include/boost
}
