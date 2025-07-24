# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>
# Contributor: peippo <christoph+aur@christophfink.com>

_cranname=data.table
_cranver=1.17.8
pkgname=r-${_cranname,,}
pkgdesc="Extension of ‘data.frame’"
url="https://cran.r-project.org/package=${_cranname}"
license=("MPL-2.0")
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
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('62e3cda4b9daee7e760b9c9ae2686ca011bca6d3704d11588b371c4b4f0fee0881f9fa224713917ffd9d90e299fbc6dcea394c6a125f525329601fa27afdb922')

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
