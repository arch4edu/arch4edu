# Maintainer: Elio <ancibrothers@gmail.com>
# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=R6
_cranver=2.6.1
pkgname=r-${_cranname,,}
pkgdesc="Encapsulated Classes with Reference Semantics"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=5

arch=("any")
depends=(
    "r>=3.6"
)
optdepends=(
    "r-lobstr"
    "r-testthat>=3.0.0"
)

# The unittests for `r-r6` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-r6`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat"
# )

# It uses cloud.r-project.org instead of cran to make use of the CDN.
source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("5cd595f908bd17908e9eaf5ccacbccfd6eea794584e7e7f1ff0bf20c3286f6fd11e63b2190d85f7bd0ddd33744c1c2d53e269c2107dbda9e84885599d8a28abb")

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
