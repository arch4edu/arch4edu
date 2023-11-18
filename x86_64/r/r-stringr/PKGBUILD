# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=stringr
_cranver=1.5.1
pkgname=r-${_cranname,,}
pkgdesc="Simple, Consistent Wrappers for Common String Operations"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.6"
    "r-cli"
    "r-glue>=1.6.1"
    "r-lifecycle>=1.0.3"
    "r-magrittr"
    "r-rlang>=1.0.0"
    "r-stringi>=1.5.3"
    "r-vctrs>=0.4.0"
)
optdepends=(
    "r-covr"
    "r-dplyr"
    "r-gt"
    "r-htmltools"
    "r-htmlwidgets"
    "r-knitr"
    "r-rmarkdown"
    "r-tibble"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("8b8b9fa545798fca619429f17c224f89b18cfff0a2890edf53ac12436df3ef9c3e1309edb42569df72fe3058ac392065d9d3482addce86067dd5918844afa771")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
