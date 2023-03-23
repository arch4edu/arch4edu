# Maintainer: peippo <christoph+aur@christophfink.com>
# Maintainer: Grey Christoforo <first name at last name dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=withr
_cranver=2.5.0
pkgname=r-${_cranname,,}
pkgdesc="Lightweight Well-Known Geometry Parsing"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=2

arch=("any")
depends=(
    "r>=3.2.0"
)
optdepends=(
    "r-callr"
    "r-covr"
    "r-dbi"
    "r-knitr"
    "r-rmarkdown"
    "r-rsqlite"
)
checkdepends=(
    "${optdepends[@]}"
    "r-testthat"
    "texlive-core"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("b472aef752317feedab16ab01557f28cdd30d8f2c6902b1a496f308165c1e02f7a8859cc791acf714748ad0a1b2d58dc9567cacfa0083a8427eb487820d8ab10")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    R_BUILD_TAR="tar" R_LIBS="build/" R CMD check "${_cranname}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
