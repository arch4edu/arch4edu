# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=fansi
_cranver=1.0.4
pkgname=r-${_cranname,,}
pkgdesc="ANSI Control Sequence Aware String Functions"
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL2" "GPL3")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.1.0"
)
optdepends=(
    "r-knitr"
    "r-rmarkdown"
    "r-unitizer"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("1a7986c7d6ac17aef79c137840cb299b16ff089b1ff1b87068af4ad79688624137b8e5da8a533dac2e29b749de81f6ef8f68f9c78a7448b1cfbd409b7205dbc0")

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
