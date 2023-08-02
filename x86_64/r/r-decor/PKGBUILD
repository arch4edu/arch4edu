# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=decor
_cranver=1.0.2
pkgname=r-${_cranname,,}
pkgdesc="Retrieve Code Decorations"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.3.0"
    "r-tibble"
    "r-vctrs>=0.5.0"
)
optdepends=(
    "r-covr"
)

checkdepends=(
    "${optdepends[@]}"
    "r-testthat"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("1cf4ee91f644265338317204e7d6351ce2c9665fce23a101cebe83073496842f716e200db391e02d0adc55d30595f3fab973078636e9327f93dd195a33819347")

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
