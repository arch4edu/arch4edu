# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=stringr
_cranver=1.5.0
pkgname=r-${_cranname,,}
pkgdesc="Simple, Consistent Wrappers for Common String Operations"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=2

arch=("i686" "x86_64")
depends=(
    "r>=3.3"
    "r-cli"
    "r-glue>=1.6.1"
    "r-lifecycle>=1.0.3"
    "r-magrittr"
    "r-rlang>=1.0.0"
    "r-stringi>=1.5.3"
    "r-vctrs"
)
optdepends=(
    "r-covr"
    "r-htmltools"
    "r-htmlwidgets"
    "r-knitr"
    "r-rmarkdown"
)
checkdepends=(
    "${optdepends[@]}"
    "r-testthat>=3.0.0"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("361e3d94de8d9e763316474eff865c6df31461e93e56a8f31cec35ace6984e2140df3d4eaf7e570693e1022a2a5323cdffc88434394b7b067c28daecd84d4784")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    R_LIBS="build/" R CMD check --no-manual --as-cran "${_cranname}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
