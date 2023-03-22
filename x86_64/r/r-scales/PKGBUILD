# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname="scales"
_cranver=1.2.1
pkgname="r-${_cranname,,}"
pkgdesc="Scale Functions for Visualization"
pkgver="${_cranver//[:-]/.}"
pkgrel=2

arch=("any")
license=("MIT")

url="https://cran.r-project.org/package=${_cranname}"
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("db15b378fafb37a4adb5bb426582d2ab4ef53ba76ac88fabfe2c87f813e0863f8d89dd2a24cae9e9657c4f0bf889dba1b5d75cc1345496dc163d61b45b1ace33")

depends=(
    "r>=3.2"
    "r-farver>=2.0.3"
    "r-labeling"
    "r-lifecycle"
    "r-munsell>=0.5"
    "r-r6"
    "r-rcolorbrewer"
    "r-rlang>=1.0.0"
    "r-viridislite"
)
optdepends=(
    "r-bit64"
    "r-covr"
    "r-dichromat"
    "r-ggplot2"
    "r-hms>=0.5.0"
    "r-stringi"
    "r-waldo>=0.4.0"
)
checkdepends=(
    "${optdepends[@]}"
    "r-testthat>=3.0.0"
)

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    R_LIBS="build/" R CMD check --no-manual --as-cran "${_cranname}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
