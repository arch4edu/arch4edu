# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=data.table
_cranver=1.14.4
pkgname=r-${_cranname,,}
pkgdesc="Extension of 'data.frame'"
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
    "r-curl"
    "r-knitr"
    "r-nanotime"
    "r-r.utils"
    "r-rmarkdown"
    "r-xts"
    "r-yaml"
    "r-zoo>=1.8.1"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('f402d25b930ae35f40058b5923fb099f94d0229d9c736750967b371c513b68b6510224c4850c6757a2c13adc70ecdcbeb416a6c09f29684616c4dcbe92b795f5')

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
