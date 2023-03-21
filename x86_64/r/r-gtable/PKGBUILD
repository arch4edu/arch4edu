# Maintainer: <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=gtable
_cranver=0.3.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=3
pkgdesc="Arrange ‘Grobs’ in Tables"
arch=("any")
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=3.5"
    "r-cli"
    "r-glue"
    "r-lifecycle"
    "r-rlang"
)
optdepends=(
    "r-covr"
    "r-ggplot2"
    "r-knitr"
    "r-profvis"
    "r-rmarkdown"
)
checkdepends=(
    "r-testthat>=3.0.0"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("b955cc53bae14486a1d332f3e57248893d8ede557b23937a16a596f984e686b747a6d2ca2d390a171b678813a134b6dd1044d78e8387928119137bb1b575cce7")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    cd "${srcdir}/${_cranname}/tests"
    R_LIBS="${srcdir}/build" Rscript --vanilla testthat.R
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
