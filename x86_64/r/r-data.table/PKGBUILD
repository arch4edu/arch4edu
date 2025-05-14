# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>
# Contributor: peippo <christoph+aur@christophfink.com>

_cranname=data.table
_cranver=1.17.2
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
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('a4888f910341fa4e6e351d284bc6bcc03954bde6892e679b7ed5b220ebe356d969dbd2d6087d4c01921d83f4ddd07e717d71d504ce7be239af0eb80dbe34904e')

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
