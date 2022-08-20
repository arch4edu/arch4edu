# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname="scales"
_cranver=1.2.1
pkgname="r-${_cranname,,}"
pkgdesc="Scale Functions for Visualization"
pkgver="${_cranver//[:-]/.}"
pkgrel=1

arch=("any")
license=("MIT")

url="https://cran.r-project.org/package=${_cranname}"
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=("59453e6dbdafee93dfb101e4d86048a62a12898134259d3ef02d65aeec57ed08")

depends=(
    "r>=3.2"
    "r-farver>=2.0.3"
    r-labeling
    r-lifecycle
    "r-munsell>=0.5"
    r-r6
    r-rcolorbrewer
    "r-rlang>=1.0.0"
    r-viridislite
)
optdepends=(
    r-bit64
    r-covr
    r-dichromat
    r-ggplot2
    "r-hms>=0.5.0"
    r-stringi
    "r-testthat>=3.0.0"
    "r-waldo>=0.4.0"
)

build() {
    R CMD INSTALL "${_cranname}_${_cranver}.tar.gz" -l "${srcdir}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 \
            "${_cranname}/LICENSE" \
            "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
