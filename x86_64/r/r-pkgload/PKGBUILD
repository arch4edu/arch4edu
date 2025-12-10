# Maintainer: Elio <ancibrothers@gmail.com>
# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=pkgload
_cranver=1.4.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Simulate Package Installation and Attach"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
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

source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("420c80559a16a9feeced024a9e34dd175968a31d90bafd80522a86c03a65db617b7ee7a72df279e86dd4010765a1a1dde1dfb5cd4e91f826751684ef45e19bf9")

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
