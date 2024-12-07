# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=data.table
_cranver=1.16.4
pkgname=r-${_cranname,,}
pkgdesc="Extension of ‘data.frame’"
url="https://cran.r-project.org/package=${_cranname}"
license=("MPL2")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.3.0"
    "zlib"
)
optdepends=(
    "r-bit64>=4.0.0"
    "r-bit>=4.0.4"
    "r-knitr"
    "r-r.utils"
    "r-rmarkdown"
    "r-xts"
    "r-yaml"
    "r-zoo>=1.8.1"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("2f5c185e2ed9bc5abace376e5533d07a3b9732a6ff31d5ddb86f27365848127b12fe07ddbcd6d8c02998337363822bd422015a5cd780fc83776898ccc46b9375")

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
