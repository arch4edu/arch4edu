# Maintainer: Jose Riha <jose1711 gmail com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Grey Christoforo <first name at last name dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=withr
_cranver=3.0.3
pkgname=r-${_cranname,,}
pkgdesc="Run Code 'With' Temporarily Modified Global State"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r>=3.6.0"
)
optdepends=(
    "r-callr"
    "r-dbi"
    "r-knitr"
    "r-rlang"
    "r-rmarkdown>=2.12"
    "r-rsqlite"
)

# The unittests for `r-withr` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-withr`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
#     "texlive-core"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("12d91b7600b57b4816c5d9fcb1fbb1f4af0fb5a9dd1b28e79fe08d89a0c85ba35a202b2a48e9a6988e341ac50497d5ffdd5e1cc2776b89d5b45f2720d1a98b16")

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
    if [[ -f "${srcdir}/${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${srcdir}/${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
