# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=farver
_cranver=2.1.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="High Performance Colour Space Manipulation"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    r
)
optdepends=(
    r-covr
)
checkdepends=(
    "${optdepends[@]}"
    "r-testthat>=3.0.0"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("8aae9b293163faaefa87227286e8c49fc7432689338120a07ec00f6337828eaf5bcee2ef1ab2ceadfe1846546fe1397647d324c69a43735f3e595d3361bcc3b5")

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
