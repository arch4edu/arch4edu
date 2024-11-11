# Maintainer: <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=gtable
_cranver=0.3.6
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Arrange ‘Grobs’ in Tables"
arch=("any")
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=4.0"
    "r-cli"
    "r-glue"
    "r-lifecycle"
    "r-rlang>=1.1.0"
)
optdepends=(
    "r-covr"
    "r-ggplot2"
    "r-knitr"
    "r-profvis"
    "r-rmarkdown"
)

# The unittests for `r-gtable` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-gtable`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("24f9fb50fd39d4a254f22c7124fcf8693de5f0d490e7dbb6f0710fae1304101517302a94bd91f0f71d4d35c4b232ac5aef0e87f3bcd111c61c84cefea2728e44")

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
