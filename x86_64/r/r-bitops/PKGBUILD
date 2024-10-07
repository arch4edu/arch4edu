# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=bitops
_cranver=1.0-9
pkgname=r-${_cranname,,}
pkgdesc="Bitwise Operations"
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL2" "GPL3")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("6fd3b6768c2a814b59b1288e3b1db669e05e01ac3aaf1e0f5fb3471e826d2055f21a8980c1342c954fe2ca1f5ec513f2b5ff67e0fee3354cd24f13e95da0dc81")

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
