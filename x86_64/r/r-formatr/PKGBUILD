# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>


_cranname=formatR
_cranver=1.14
pkgname=r-${_cranname,,}
pkgdesc="Format R Code Automatically"
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r>=3.2.3"
)
optdepends=(
    "r-knitr"
    "r-rmarkdown"
    "r-rstudioapi"
    "r-shiny"
    "r-testit"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("3a232a3bb0cb1f1b3c587761d5f0992f2de3047a78181b285b52d9acaf5b5c448c91dc84da53c109a9dbdf302ec8da183997f7ef027927f852f8e68504637962")

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
