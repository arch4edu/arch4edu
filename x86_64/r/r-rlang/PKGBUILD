# Maintainer: <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=rlang
_cranver=1.1.0
pkgname=r-${_cranname,,}
pkgdesc="Functions for Base Types and Core R and ‘Tidyverse’ Features"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.5.0"
)
optdepends=(
    "r-cli>=3.1.0"
    "r-covr"
    "r-crayon"
    "r-fs"
    "r-glue"
    "r-knitr"
    "r-magrittr"
    "r-pillar"
    "r-rmarkdown"
    "r-testthat>=3.0.0"
    "r-tibble"
    "r-usethis"
    "r-vctrs>=0.2.3"
    "r-withr"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('6aad4eee4a97b7082160e2a2354c7165322a3e55e84239a38edda18eda5cbc8fdacc0bc8bbc246dfec41e9ec366d64dfe3e2e366f8d914f2b2ff9f5310582ab8')

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
