# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=BH
_cranver=1.78.0-0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Boost C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(Boost)
depends=(boost r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('3b9e9d07682013e0c06a396dda176b405eab99a7273eca6c40d1b4c4110e8cb3')

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
