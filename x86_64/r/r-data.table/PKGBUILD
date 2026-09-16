# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>
# Contributor: peippo <christoph+aur@christophfink.com>

_cranname=data.table
_cranver=1.18.6.1
pkgname=r-${_cranname,,}
pkgdesc="Extension of ‘data.frame’"
url="https://cran.r-project.org/package=${_cranname}"
license=("MPL-2.0")
pkgver=${_cranver//[:-]/.}
pkgrel=1
arch=("i686" "x86_64")
depends=(
    "r>=3.4.0"
    "zlib"
)
optdepends=(
    "r-bit64>=4.0.0"
    "r-bit>=4.0.4"
    "r-knitr"
    "r-r.utils>=2.13.0"
    "r-rmarkdown"
    "r-xts"
    "r-yaml"
    "r-zoo>=1.8.1"
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('f6766201deae2bcd398f4355daf8e0daa125b776453de978d1274b632fe3dc740a5eb8671446418b14357db10dc35c2b86edfdb69963f9ce10225f6394936e76')

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
