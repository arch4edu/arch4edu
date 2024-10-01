# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=bitops
_cranver=1.0-8
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
b2sums=("19dcd4a33880d6c2628e41cadcd541e99fb10ea0a2a7ac296b355181cd757aa4632c418e8a6af3d4487e6b05d51b0f32d71a33aeb0b31ffe27f8bb55b9e77f50")

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
