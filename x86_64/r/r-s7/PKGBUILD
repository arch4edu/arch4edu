# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=S7
_cranver=0.2.0
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
b2sums=('3881bba06e21e7d80a8a2ef691f03ba3f9d669e37b0f33714584cd73589cfce46afb0987c73fa72f46d163b28b816bbb04549eeed7da273e38d3efe79fda71b1')

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
