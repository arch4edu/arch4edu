# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=cli
_cranver=3.5.0
pkgname=r-${_cranname,,}
pkgdesc="Helpers for Developing Command Line Interfaces"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.4"
)
optdepends=(
    "r-callr"
    "r-covr"
    "r-crayon"
    "r-digest"
    "r-glue>=1.6.0"
    "r-htmltools"
    "r-htmlwidgets"
    "r-knitr"
    "r-mockery"
    "r-processx"
    "r-ps>=1.3.4.9000"
    "r-rlang>=1.0.2.9003"
    "r-rmarkdown"
    "r-rprojroot"
    "r-rstudioapi"
    "r-testthat"
    "r-tibble"
    "r-whoami"
    "r-withr"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('1fa821d33414cb9acc7a933889090e689a18c781e5e81dc2ab59a60e8df5fa11d1bae00f1424fd8a0828ec70b019eb31252311f835c1f71883c13fe7a7745ffa')

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
