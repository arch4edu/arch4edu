# Maintainer: Christos Longros <chris.longros@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=vctrs
_pkgver=0.7.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Vector Helpers"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
    "r>=4.0.0"
    "r-cli>=3.4.0"
    "r-glue"
    "r-lifecycle>=1.0.3"
    "r-rlang>=1.1.7"
)
optdepends=(
    "r-bit64"
    "r-covr"
    "r-crayon"
    "r-dplyr>=0.8.5"
    "r-generics"
    "r-knitr"
    "r-pillar>=1.4.4"
    "r-pkgdown>=2.0.1"
    "r-rmarkdown"
    "r-tibble>=3.1.3"
    "r-waldo>=0.2.0"
    "r-withr"
    "r-xml2"
    "r-zeallot"
)

# Due to a circular dependency on itself, r-vctrs cannot
# be checked on first build

# To run the unittests during subsequent builds, uncomment
# the lines below, as well as the `check()` function further
# down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
b2sums=('3aa6a262f852c92e6c7a09f45dabc047f2405a606048272c9d784344aa2eac145837cdb1c00a89f8b66e1cd0343c3276d2f690b73aded24eb9896a275068390c')

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     cd "${srcdir}/${_pkgname}/tests"
#     R_LIBS="${srcdir}/build" Rscript --vanilla testthat.R
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_pkgname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_pkgname}/LICENSE" ]]; then
        install -Dm0644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
