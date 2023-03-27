# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=remotes
_cranver=2.4.2
pkgname=r-${_cranname,,}
pkgdesc="R package installation from remote repositories, including GitHub"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=3

arch=("any")
depends=(
    "r>=3.0.0"
)
optdepends=(
    "r-brew"
    "r-callr"
    "r-codetools"
    "r-curl"
    "r-covr"
    "r-git2r>=0.23.0"
    "r-knitr"
    "r-mockery"
    "r-pkgbuild>=1.0.1"
    "r-pingr"
    "r-rmarkdown"
    "r-rprojroot"
    "r-testthat"
    "r-webfakes"
    "r-withr"
)

# The unittests for `r-remotes` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-remotes`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("f189cbdd6d687145a031f6e3e267e68db891f526e61acf16e93c7af3aa1af8fbffb713d8b00af9d9ad52c4dd1fedad72fed528b319f996ef6b0060ebf607102d")

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
