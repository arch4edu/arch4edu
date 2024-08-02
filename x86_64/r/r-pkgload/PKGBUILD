# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=pkgload
_cranver=1.4.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Simulate Package Installation and Attach"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL-3.0-only")
depends=(
    "r>=3.4.0"
    "r-cli>=3.3.0"
    "r-desc"
    "r-fs"
    "r-glue"
    "r-lifecycle"
    "r-pkgbuild"
    "r-processx"
    "r-rlang>=1.0.3"
    "r-rprojroot"
    "r-withr>=2.4.3"
)
optdepends=(
    "r-bitops"
    "r-jsonlite"
    "r-mathjaxr"
    "r-pak"
    "r-rcpp"
    "r-remotes"
    "r-rstudioapi"
    "r-usethis"
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

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("620aaefc9dd10573d941d78a8fcb93b87c3e455c9e58a86a492ca5e56bc5adb4f4cf65ac0311891fb564d433ae4dd776d38ef3d98050ae33f7dc56fc9547aada")

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
