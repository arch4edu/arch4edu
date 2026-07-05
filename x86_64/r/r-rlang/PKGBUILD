# Maintainer: Christos Longros <chris.longros at gmail dot com>
# Maintainer: a821 <a821 at mail dot de>
# Contributor: Elio <ancibrothers@gmail.com>
# Contributor: <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=rlang
_cranver=1.3.0
pkgname=r-${_cranname,,}
pkgdesc="Functions for Base Types and Core R and ‘Tidyverse’ Features"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
depends=(
    "r>=4.0.0"
)
optdepends=(
    "r-cli>=3.1.0"
    "r-covr"
    "r-crayon"
    "r-desc"
    "r-fs"
    "r-glue"
    "r-knitr"
    "r-magrittr"
    "r-pillar"
    "r-pkgload"
    "r-rmarkdown"
    "r-testthat>=3.3.2"
    "r-tibble"
    "r-usethis"
    "r-vctrs>=0.2.3"
    "r-withr"
)

# The unittests for `r-rlang` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-rlang`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

# It uses cloud.r-project.org instead of cran to make use of the CDN.
source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('3bc6cba32f08de9789ddc6a9a3f095c5dfab0e2d93496fdc4438626f732458a373012869105e708291a8c393706c6dca5503a32d6b6570b2c6231bcf3000503c')

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
