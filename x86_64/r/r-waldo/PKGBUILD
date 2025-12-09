# Maintainer: Elio <ancibrothers@gmail.com>
# Maintainer: peippo <christoph+aur@christophfink.com>
# Maintainer: Grey Christoforo <first name at last name dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=waldo
_cranver=0.6.2
pkgname=r-${_cranname,,}
pkgdesc="Anything to ‘POSIXct’ or ‘Date’ Converter"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r>=4.0"
    "r-cli"
    "r-diffobj>=0.3.4"
    "r-glue"
    "r-rlang>=1.1.0"
)
optdepends=(
    "r-bit64"
    "r-r6"
    "r-s7"
    "r-testthat>=3.0.0"
    "r-withr"
    "r-xml2"
)

# The unittests for `r-waldo` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-waldo`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat"
# )

source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("fe4bd4b98135cb652b57999e314f3af81fb515375dbae5457e6b3632887236a90329df7a46914ce572fcceddd745ec364df226c1863ea0d51d904ef0e4944410")

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
