# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>


_cranname=stringi
_cranver=1.7.12
pkgname=r-${_cranname,,}
pkgdesc="Fast and Portable Character String Processing Facilities"
url="https://cran.r-project.org/package=${_cranname}"
license=("custom")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "icu>=55"
    "r>=3.1"
    "r-cpp11"
)
optdepends=()
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('7d368e7e5bb439c7e64c68f2a26eae4e7b48a109cde617aa75dcbce839794711accaf1725df9033bcf8277d82430436b61de037f02ad6724bb988fe4b5854879')

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
