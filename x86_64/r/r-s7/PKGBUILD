# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=S7
_cranver=0.2.1
pkgname=r-${_cranname,,}
pkgdesc="An Object Oriented System Meant to Become a Successor to S3 and S4"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r"
)
optdepends=(
    "r-bench"
    "r-covr"
    "r-knitr"
    "r-rmarkdown"
    "r-tibble"
)

checkdepends=(
    "${optdepends[@]}"
    "r-testthat"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('e263c664ec6d45631cb1422838579f99fb1b63f35118af747649c9df249e0166ec932fb9b7e7a1521f5fb77a32a0d7531d62edea0cd5c90f47c3a7781e9a8035')

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    export R_LIBS="build/"
    R CMD check --no-manual "${_cranname}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
