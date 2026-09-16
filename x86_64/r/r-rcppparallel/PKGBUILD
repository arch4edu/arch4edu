# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=RcppParallel
pkgname=r-${_pkgname,,}
pkgdesc="Parallel Programming Tools for Rcpp"
pkgver=6.2.1
pkgrel=1
url="https://cran.r-project.org/package=${_pkgname}"
license=("GPL3")

arch=("i686" "x86_64")
depends=(
    "r>=3.0.2"
    "tbb"
)
optdepends=(
    "r-knitr"
    "r-markdown"
    "r-rcpp"
    "r-runit"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_pkgname}_${pkgver}.tar.gz")
sha256sums=('6d076439020f64f502552ae924e93f62b6fefd2bb5c193987751dc7a48826ebc')

build() {
    # link against the system TBB instead of building the bundled copy
    export TBB_LIB=/usr/lib TBB_INC=/usr/include
    R CMD INSTALL ${_pkgname}_${pkgver}.tar.gz \
    --library="${srcdir}" \
    --no-byte-compile \
    --no-test-load
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_pkgname}/LICENSE" ]]; then
        install -Dm0644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
