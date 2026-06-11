# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=colorspace
_cranver=2.1-2
pkgname=r-${_cranname,,}
pkgdesc="A Toolbox for Manipulating and Assessing Colors and Palettes"
url="https://cran.r-project.org/package=${_cranname}"
license=("BSD")
pkgver=${_cranver//[:-]/.}
pkgrel=2

arch=("i686" "x86_64")
depends=(
    "r>=3.0.0"
)
optdepends=(
    "r-cartocolor"
    "r-colorbrewer"
    "r-dplyr"
    "r-ggplot2"
    "r-jpeg"
    "r-kernlab"
    "r-kernsmooth"
    "r-knitr"
    "r-markdown"
    "r-mass"
    "r-mvtnorm"
    "r-png"
    "r-scales"
    "r-scico"
    "r-shiny"
    "r-shinyjs"
    "r-vcd"
    "r-viridis"
    "r-wesanderson"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('0d68b13ed0a9bf743362e35a574f5889a338e48ce74d98a2647add3dd1133b6927d7e53adbb366c881cabbc42c3f0b1b84003923edf2fa516e11a4b2991ab610')

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
