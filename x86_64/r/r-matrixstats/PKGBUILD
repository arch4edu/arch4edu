# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=matrixStats
_cranver=1.4.1
pkgname=r-${_cranname,,}
pkgdesc="Functions that Apply to Rows and Columns of Matrices (and to Vectors)"
url="https://cran.r-project.org/package=${_cranname}"
license=("Artistic-2.0")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=2.12.0"
)
optdepends=(
    "r-base64enc"
    "r-ggplot2"
    "r-knitr"
    "r-markdown"
    "r-microbenchmark"
    "r-r.devices"
    "r-r.rsp"
    "r-utils"
)

# The unittests for `r-matrixstats` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-matrixstats`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "qpdf"
#     "r-rcmdcheck"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("b888fb8b64c0da31fdf40070242f3f14755e2ca2af46259a5d9f0e97e4bf77e69b6fcb5b878641ec82f505e0b33b1cea7bbd179ab487025d816dc55d8faa9fc0")

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
