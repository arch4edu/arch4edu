# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=desc
_cranver=1.4.2
pkgname=r-${_cranname,,}
pkgdesc="Manipulate DESCRIPTION Files"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r>=3.4.0"
    "r-cli"
    "r-r6"
    "r-rprojroot"
)
optdepends=(
    "r-callr"
    "r-covr"
    "r-gh"
    "r-spelling"
    "r-testthat"
    "r-whoami"
    "r-withr"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('35d1f2f80c2bd9b59c8e7589fe573d90816cebd1fd763a232243a074dfd2ec052dce1424988e931a429c3898845a44bbbc6628405a93b4693a4dabaf5fdc59f3')

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
