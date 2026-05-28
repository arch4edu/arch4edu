# Maintainer: Christos Longros <chris.longros@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=stringr
_pkgver=1.6.0
pkgname=r-${_pkgname,,}
pkgdesc="Simple, Consistent Wrappers for Common String Operations"
url="https://cran.r-project.org/package=${_pkgname}"
license=("MIT")
pkgver=${_pkgver//-/.}
pkgrel=2

arch=("i686" "x86_64")
depends=(
    "r>=4.1.0"
    "r-cli"
    "r-glue>=1.6.1"
    "r-lifecycle>=1.0.3"
    "r-magrittr"
    "r-rlang>=1.0.0"
    "r-stringi>=1.5.3"
    "r-vctrs>=0.4.0"
)
optdepends=(
    "r-covr"
    "r-dplyr"
    "r-gt"
    "r-htmltools"
    "r-htmlwidgets"
    "r-knitr"
    "r-rmarkdown"
    "r-tibble"
)

source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
b2sums=('7b8675448275c5ac310e86c4f7d6d0065c9c1796c2f65f814e829584a831d078bcd418b38f099906bfe89ec2a739d656cbba6738d0bab99dbd0b97b533752044')

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}/build/"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_pkgname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_pkgname}/LICENSE" ]]; then
        install -Dm0644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
