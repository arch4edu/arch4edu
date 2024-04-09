# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=data.table
_cranver=1.15.4
pkgname=r-${_cranname,,}
pkgdesc="Extension of ‘data.frame’"
url="https://cran.r-project.org/package=${_cranname}"
license=("MPL2")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.1.0"
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
b2sums=("3a4372d548711d6b00a9204e97848c413505620775771317d62e6b52ec449bd8331c9c565a3e19c967473f999f053bae0d05aacc3696d104c7e25bfffc70c03f")

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
