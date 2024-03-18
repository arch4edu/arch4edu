# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=remotes
_cranver=2.5.0
pkgname=r-${_cranname,,}
pkgdesc="R package installation from remote repositories, including GitHub"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

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
b2sums=("ee0959efb26f76e193c122797648bd1a52bc72154d5dce7707bc2198f7d79a9e33414157c6d964989709f4a06af3a429cbb74dc3b0c4c555861f11e0c5e3cc7c")

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
