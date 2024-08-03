# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=colorspace
_cranver=2.1-1
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
b2sums=("d18a20e16912775946f2afff2ad25e84d3275020134ae74a2e48d354414e8ce69334a3589bbfdff6617d1d447029abe29a95573854fe139054c6848348844bfb")

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
