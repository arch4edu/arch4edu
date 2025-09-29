# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
_cranname="scales"
_cranver=1.4.0
pkgname="r-${_cranname,,}"
pkgdesc="Scale Functions for Visualization"
pkgver="${_cranver//[:-]/.}"
pkgrel=1
arch=(any)
license=(MIT)
url="https://cran.r-project.org/package=${_cranname}"
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('54f80ee76dcc35e25e30e6d963cebb3e367f11785c8cf3d54ac4720011da3d49e266b4f1afd3d0b7f548125cec9e5b400c9ccfefd6d55bdc357ae23cc9c3ff24')
depends=(
    "r>=4.1"
    "r-cli"
    "r-farver>=2.0.3"
    "r-glue"
    "r-labeling"
    "r-lifecycle"
    "r-r6"
    "r-rcolorbrewer"
    "r-rlang>=1.0.0"
    "r-viridislite"
)
optdepends=(
    "r-bit64"
    "r-covr"
    "r-dichromat"
    "r-ggplot2"
    "r-hms>=0.5.0"
    "r-stringi"
    "r-testthat>=3.0.0"
)

# The unittests for `r-scales` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-scales`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

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
