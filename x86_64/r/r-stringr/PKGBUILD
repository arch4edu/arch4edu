# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=stringr
_cranver=1.4.1
pkgname=r-${_cranname,,}
pkgdesc="Simple, Consistent Wrappers for Common String Operations"
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL2")
pkgver=${_cranver//[:-]/.}
pkgrel=2

arch=("i686" "x86_64")
depends=(
    r
    "r-glue>=1.2.0"
    r-magrittr
    "r-stringi>=1.1.7"
)
optdepends=(
    r-covr
    r-htmltools
    r-htmlwidgets
    r-knitr
    r-rmarkdown
    r-testthat
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("ce3c4917fc21e26eec110a2d49b4f125718368665b324c1110524e411a358ef70db7b750e85474b5061bf1400896739766459a6a7bc5a8e88dad4d114cdc18a1")

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
