# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=crayon
_cranver=1.5.2
pkgname=r-${_cranname,,}
pkgdesc="Colored Terminal Output"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r"
)
optdepends=(
    "r-mockery"
    "r-rstudioapi"
    "r-testthat"
    "r-withr"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('8727fa876071c22be0a937d85edaf4c041f4798b72b25281233f3d15387dc49589b933e722591e3297d9d987b4a7c6fe7c20d5ae8acde59d08dc5e463f6e1fa2')

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
