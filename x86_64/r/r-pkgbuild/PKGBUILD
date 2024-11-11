# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=pkgbuild
_cranver=1.4.5
pkgname=r-${_cranname,,}
pkgdesc="Find Tools Needed to Build R Packages"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r>=3.5"
    "r-callr>=3.2.0"
    "r-cli>=3.4.0"
    "r-desc"
    "r-processx"
    "r-r6"
)
optdepends=(
    "r-covr"
    "r-cpp11"
    "r-knitr"
    "r-rcpp"
    "r-rmarkdown"
    "r-withr>=2.3.0"
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
#     "r-testthat>=3.2.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("1835d6e58a47fcb23f687dac1ddad797d40ac2ba4a9d227c183c2f2e09f7970d6f5bd487b1250195d5858d1096a8ba44e7910ae2837bf71f20feadd338cde3e5")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     export R_LIBS="build/"
#     rm "${srcdir}/${_cranname}/tests/testthat/test-build.R"  # fails in current toolchain
#     R CMD check --no-manual "${_cranname}"
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
