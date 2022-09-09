# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=cli
_cranver=3.4.0
pkgname=r-${_cranname,,}
pkgdesc="Helpers for Developing Command Line Interfaces"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.4"
)
optdepends=(
    "r-callr"
    "r-covr"
    "r-digest"
    "r-glue>=1.6.0"
    "r-htmltools"
    "r-htmlwidgets"
    "r-knitr"
    "r-mockery"
    "r-processx"
    "r-projroot"
    "r-ps>=1.3.4.9000"
    "r-rlang>=1.0.2.9003"
    "r-rmarkdown"
    "r-rstudioapi"
    "r-testthat"
    "r-tibble"
    "r-whoami"
    "r-withr"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("83ca81c0331c03bf203f101359e2020f1bc3e65ec9221582044012116731e943a6777d31a0db5b5b1513c56c1f1bb3d54486bd91804573d748d6fded131800a7")

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
