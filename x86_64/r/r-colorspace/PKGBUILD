# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=colorspace
_cranver=2.1-0
pkgname=r-${_cranname,,}
pkgdesc="A Toolbox for Manipulating and Assessing Colors and Palettes"
url="https://cran.r-project.org/package=${_cranname}"
license=("BSD")
pkgver=${_cranver//[:-]/.}
pkgrel=1

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
b2sums=("942cadbdf54545aa596a6aeedc520bb7c1738bd663c1e172f4e1336bb778f6a167f01d74950ece04823490437f9bdae930e92946c9c0ec5dbc04ab8e35c981b3")

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
