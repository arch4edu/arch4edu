# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=future.apply
_cranver=1.11.1
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
b2sums=("b74abb59493f7ab6d278376fcc49159f22bc76f3e2563b750b6735820b056f0d5ace7cbae4813c15076220c0e8ca0ce00124a6e51ecee1f7f74f3dfb460e21f8")

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
