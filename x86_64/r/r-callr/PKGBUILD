# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=callr
_cranver=3.7.3
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Call R from R"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r-processx r-r6)
optdepends=(
    r-asciicast
    r-cli
    r-covr
    r-mockery
    r-ps
    r-rprojroot
    r-spelling
    r-testthat
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('567bfedf073a1d4c5785f0553341608a214938110567b9a6495ff20ebb2fd04e'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  install -Dm644 CRAN-MIT-TEMPLATE "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
