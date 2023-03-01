# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=fontLiberation
_cranver=0.1.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Liberation Fonts"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(custom:OFL)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('acdea423e005873aa509e280074a3cef4796e4f7e9d77b3945d77b451ea039f0')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
