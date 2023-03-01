# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=fontBitstreamVera
_cranver=0.1.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Fonts with 'Bitstream Vera Fonts' License"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(custom)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('3298b3dd95605bdda0c5fce5594c9bedde6aa63d89b216d5c83c6c092b6d375a')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  install -Dm644 "${_cranname}/LICENCE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENCE"
}
