# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=cli
_cranver=3.6.0
pkgname=r-${_cranname,,}
pkgdesc="Helpers for Developing Command Line Interfaces"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=2

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
    "r-tibble"
    "r-whoami"
    "r-withr"
)
checkdepends=(
    "${optdepends[@]}"
    "r-testthat"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("e04e67732c8dc8c649aea11487a03606cc959c1f1e3eca162027530329c638da5225465e0f53e3f7aa937e2dda322346d9df6ce6d931d5e013dabdfa1116879d")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    cd "${srcdir}/${_cranname}/tests"
    R_LIBS="${srcdir}/build/" Rscript --vanilla testthat.R
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
