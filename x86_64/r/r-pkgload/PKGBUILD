# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=pkgload
_cranver=1.3.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Simulate Package Installation and Attach"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(
    "r>=3.4.0"
    "r-cli>=3.3.0"
    r-crayon
    r-desc
    r-fs
    r-glue
    "r-rlang>=1.0.3"
    r-rprojroot
    "r-withr>=2.4.3"
)
optdepends=(
    r-bitops
    r-covr
    r-mathjaxr
    r-pak
    r-pkgbuild
    r-rcpp
    r-remotes
    r-rstudioapi
    "r-testthat>=3.1.0"
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=("5af653c901662260cc221971cc968355428cc6183b61c15be80aa9545f9f4228")

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
