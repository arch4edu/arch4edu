# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=units
_cranver=0.8-2
pkgname=r-${_cranname,,}
pkgdesc="Measurement Units for R Vectors"
url="https://cran.r-project.org/package=units"
license=("GPL2")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=3.0.2"
    "r-rcpp>=0.12.10"
    "udunits"
)
optdepends=(
    "r-dplyr>=1.0.0"
    "r-ggplot2>=3.2.1"
    "r-knitr"
    "r-magrittr"
    "r-measurements"
    "r-nistunits"
    "r-pillar>=1.3.0"
    "r-rmarkdown"
    "r-vctrs>=0.3.1"
    "r-vdiffr"
    "r-xml2"
)

# The unittests for `r-units` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-units`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("a7ae8953afb2ef6e993dab6512d5b6af54045db4e462af104bd8141c4fe4b0d9c8ba4bf0610d03730c5e43c4bbd2d2b06227bb89859292218e32e1cff1353680")

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
