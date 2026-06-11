# Maintainer: Christos Longros <chris.longros@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=fansi
_pkgver=1.0.7
pkgname=r-${_pkgname,,}
pkgdesc="ANSI Control Sequence Aware String Functions"
url="https://cran.r-project.org/package=${_pkgname}"
license=("GPL2" "GPL3")
pkgver=${_pkgver//-/.}
pkgrel=2

arch=("i686" "x86_64")
depends=(
    "r>=3.1.0"
)
optdepends=(
    "r-knitr"
    "r-rmarkdown"
    "r-unitizer"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
b2sums=('4760d6ab35540e1ebe67cadd574ea29203c7cc533e7b1371b002fa59201f213690638860dbaaed25f0cde5e3aee09d73fd598dd70fb6681569ecf4ccd66a3a92')

build() {
    R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_pkgname}/LICENSE" ]]; then
        install -Dm0644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
