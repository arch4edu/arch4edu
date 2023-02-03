# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=utf8
_cranver=1.2.3
pkgname=r-${_cranname,,}
pkgdesc="Unicode Text Processing"
url="https://cran.r-project.org/package=${_cranname}"
license=("Apache")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=2.10"
)
optdepends=(
    "r-cli"
    "r-covr"
    "r-knitr"
    "r-rlang"
    "r-rmarkdown"
    "r-testhat>=3.0.0"
    "r-withr"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('14d380cb019ecc96bb7faaf8ae948b1789180e482a846346b3d26d42c9af7d8239bb57faecff499e59bf6a2b2afea16e44c3c122ba1a485746943a3be9328287')

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
