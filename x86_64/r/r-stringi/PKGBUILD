# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>


_cranname=stringi
_cranver=1.8.2
pkgname=r-${_cranname,,}
pkgdesc="Fast and Portable Character String Processing Facilities"
url="https://cran.r-project.org/package=${_cranname}"
license=("custom")
pkgver=${_cranver//[:-]/.}
pkgrel=3

arch=("i686" "x86_64")
depends=(
    "icu>=61"
    "r>=3.4"
)
optdepends=()
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("dd3bd2080c98ed3ddb591c6e4d1aa27c4f74479f615b7942864de833f466f51f2fff95dd0d4447acd3c02542dc2ff4328265b061a381e8e216f198a14f18d6c6")

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
