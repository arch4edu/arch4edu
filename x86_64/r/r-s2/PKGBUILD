# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=s2
_cranver=1.1.6
pkgname=r-${_cranname,,}
pkgdesc="Spherical Geometry Operators Using the S2 Geometry Library"
url="https://cran.r-project.org/package=s2"
license=(Apache)
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "openssl>=1.0.1"
    "r>=3.0.0"
    "r-rcpp"
    "r-wk>=0.6.0"
)
optdepends=(
    "r-bit64"
    "r-vctrs"
)

# The unittests for `r-s2` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-s2`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("a85388c14e67be04f50d93199d1c211ade95fbc045480cf5a223be04a9cb7855f9f14c186a44fdc8e8910bf1d6204221ad3a7d552c121e5b9b0dfc7e5bbaf9be")

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
