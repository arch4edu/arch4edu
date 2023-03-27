# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=pkgbuild
_cranver=1.4.0
pkgname=r-${_cranname,,}
pkgdesc="Find Tools Needed to Build R Packages"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=3

arch=("any")
depends=(
    "r>=3.4"
    "r-callr>=3.2.0"
    "r-cli>=3.4.0"
    "r-cpp11"
    "r-crayon"
    "r-desc"
    "r-prettyunits"
    "r-processx"
    "r-r6"
    "r-rprojroot"
    "r-withr>=2.3.0"
)
optdepends=(
    "r-covr"
    "r-cpp11"
    "r-knitr"
    "r-mockery"
    "r-rcpp"
    "r-rmarkdown"
)

# The unittests for `r-pkgbuild` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-pkgbuild`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("23e88c9a0bdb934823a2360ed40742695f615a1545a3d637c09c1a9af5752b1d0cbe01202b5b756b74745bdac4b3dcbdc83ce5cf9634ccadabb6d32ee46d9ad5")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     export R_LIBS="build/"
#     R CMD check --no-manual "${_cranname}"
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
