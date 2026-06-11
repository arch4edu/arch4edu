# Maintainer: Christos Longros <chris.longros@gmail.com>
# Contributor: Elio <ancibrothers@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=pkgload
_pkgver=1.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Simulate Package Installation and Attach"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=("MIT")
depends=(
    "r>=3.4.0"
    "r-cli>=3.3.0"
    "r-desc"
    "r-fs"
    "r-glue"
    "r-lifecycle"
    "r-pkgbuild"
    "r-processx"
    "r-rlang>=1.1.1"
    "r-rprojroot"
)
optdepends=(
    "r-bitops"
    "r-jsonlite"
    "r-mathjaxr"
    "r-pak"
    "r-rcpp"
    "r-remotes"
    "r-rstudioapi"
    "r-testthat>=3.2.1.1"
    "r-usethis"
    "r-withr"
)

# The unittests for `r-pkgload` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-pkgload`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.2.1.1"
# )

source=("https://cloud.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
b2sums=('02e0cdd508248c50ade3782aaabdcec19803cc3f050cec95a1db0419481cd883fbe8b3ed8482e815256fde9089545af8fb2d19b4928463f5823f772658764f31')

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     export R_LIBS="build/"
#     R CMD check --no-manual "${_pkgname}"
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_pkgname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_pkgname}/LICENSE" ]]; then
        install -Dm0644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
