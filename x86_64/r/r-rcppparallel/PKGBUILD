# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=RcppParallel
pkgname=r-${_pkgname,,}
pkgdesc="Parallel Programming Tools for Rcpp"
pkgver=5.1.11
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

source=("https://cran.r-project.org/src/contrib/Archive/${_pkgname}/${_pkgname}_${pkgver}.tar.gz")
sha256sums=("04b6d979e38d120049cb1f788873972ac3e65033d4c6878de4a3ee11e3484536")

build() {
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
