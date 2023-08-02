# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=classInt
_cranver=0.4-9
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
b2sums=('d90435a067254a1dbc7d792276245274ea4959acf20b1294c064c79224d197f44fa6dd74a1403b78c84addf3d87543aae80d6267468ed9d6e2bf1235ce2f9687')

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
