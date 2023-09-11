# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=classInt
_cranver=0.4-10
pkgname=r-${_cranname,,}
pkgdesc="Choose Univariate Class Intervals"
url="https://cran.r-project.org/package=classInt"
license=("GPL2" "GPL3")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=2.2"
    "r-class"
    "r-e1071"
    "r-kernsmooth"
)
optdepends=(
    "r-spdata>=0.2.6.2"
    "r-units"
    "r-knitr"
    "r-rmarkdown"
    "r-tinytest"
)
makedepends=("gcc-fortran")

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("394f51e137ac8451bdfb0def0662206545d28d487bf77609fc4e0cd7966960d1430c3ecbdd02c08ca7b757083fb62330dd4f598623860eaeba36b5a6d45ad7ad")

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
