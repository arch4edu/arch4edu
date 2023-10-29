# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=future.apply
_cranver=1.11.0
pkgname="r-${_cranname,,}"
pkgdesc="Apply Function to Elements in Parallel using Futures"
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL2" "GPL3")
pkgver="${_cranver//[:-]/.}"
pkgrel=1

arch=("any")
depends=(
    "r>=3.2.0"
    "r-future>=1.28.0"
    "r-globals>=0.16.1"
)
optdepends=(
    "r-listenv>=0.8.0"
    "r-r.rsp"
    "r-markdown"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("94570b6aa84fa044566f7956392ef812bfe66e92edaf773b95eb0fa176584c66c40f128e6158afb6daa802831251bf183ffb4178fbd4223e9faf5c0ef5eea1b5")

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
