# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=future.apply
_cranver=1.11.3
pkgname="r-${_cranname,,}"
pkgdesc="Apply Function to Elements in Parallel using Futures"
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL-2.0-or-later")
pkgver="${_cranver//[:-]/.}"
pkgrel=1

arch=("any")
depends=(
    "r>=3.2.0"
    "r-future>=1.28.0"
    "r-globals>=0.16.1"
)
optdepends=(
    "r-listenv>=0.8.0"
    "r-r.rsp"
    "r-markdown"
)
makedepends=()

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('da916f440caa59695b9abb348cfc1d0621e2014e1992e3ea13044ce8baa9ddd200a8da489fa6a319916b1e589231a317ba0b71cce317f54fde4473a1f3f78526')

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
