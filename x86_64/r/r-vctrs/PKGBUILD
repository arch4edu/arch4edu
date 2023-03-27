# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=vctrs
_cranver=0.6.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Vector Helpers"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=3.5.0"
    "r-cli>=3.4.0"
    "r-glue"
    "r-lifecycle>=1.0.3"
    "r-rlang>=1.1.0"
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

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("65c61c5ad4287795a134a77108badb4ea3c9ba5eb2538173785ad2aa5890bca48e3317335c664caabff336d131a72b1c35199ef9bd904af5425caac17624e01b")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     cd "${srcdir}/${_cranname}/tests"
#     R_LIBS="${srcdir}/build" Rscript --vanilla testthat.R
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
