# Maintainer: Elio <ancibrothers@gmail.com>
# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=utf8
_cranver=1.2.6
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
    "r-testthat>=3.0.0"
    "r-withr"
)
makedepends=()

source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("a25246c7881602d5543400fe0db17200a82e93dd19a30d6ff18e52790490915bfc30f5f490de0c6af139aaf8fbd5624e1fcbe4beab47c4fb99f6ca1db37a34bc")

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
