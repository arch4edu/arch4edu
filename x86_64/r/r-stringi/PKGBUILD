# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>


_cranname=stringi
_cranver=1.8.3
pkgname=r-${_cranname,,}
pkgdesc="Fast and Portable Character String Processing Facilities"
url="https://cran.r-project.org/package=${_cranname}"
license=("custom")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "icu>=61"
    "r>=3.4"
)
optdepends=()
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("e77b5a0c57f18620266797174fbc710af6edd9ba72bce0da70768b4cabd88e758f0ab856f2bee76754de431e4102d1aff66ae2d2b3d554d152081f84a4e0b75d")

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
