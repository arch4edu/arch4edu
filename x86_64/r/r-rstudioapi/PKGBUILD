# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=rstudioapi
_cranver=0.14
pkgname=r-${_cranname,,}
pkgdesc="Safely Access the RStudio API"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=2

arch=("any")
depends=(
    "r"
)
optdepends=(
    "r-clipr"
    "r-covr"
    "r-knitr"
    "r-rmarkdown"
)
checkdepends=(
    "${optdepends[@]}"
    "r-testthat"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("bb969a080d783a7f5003fb5545a37978f9fc0d6fde1e1f4d3d5b5661e14ebaa422785d103d177aff5fee0c328f5e7dc3b524f1213971d9166f52e99d1675091b")

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
