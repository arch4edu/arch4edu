# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=matrixStats
_cranver=0.63.0
pkgname=r-${_cranname,,}
pkgdesc="Functions that Apply to Rows and Columns of Matrices (and to Vectors)"
url="https://cran.r-project.org/package=${_cranname}"
license=("Artistic2.0")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=2.12.0"
)
optdepends=(
    "r-base64enc"
    "r-ggplot2"
    "r-knitr"
    "r-markdown"
    "r-microbenchmark"
    "r-r.devices"
    "r-r.rsp"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('4d2cb8b7c0f9f1e5656a0de081955a071af207089fc1ff2e4103465cb889c7a4a8a37a190d47fe0a32732137665b4ab753f39f53bbd503e5023cf7c8bfa1abef')

build() {
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
