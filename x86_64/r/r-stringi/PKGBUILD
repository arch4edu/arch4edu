# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>


_cranname=stringi
_cranver=1.8.4
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
b2sums=("7c29c7a6fda45e5550dd8012f61cf7903b74bdb5103b95ac4b971741bfb86219d7344f77764da5fc3a4754fffebde99cf0cb59143a24d484679e69d2b1c670d7")

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
