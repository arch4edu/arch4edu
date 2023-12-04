# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_cranname=testthat
_cranver=3.2.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Unit Testing for R"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=3.6.0"
    "r-brio>=1.1.3"
    "r-callr>=3.7.3"
    "r-cli>=3.6.1"
    "r-desc>=1.4.2"
    "r-digest>=0.6.33"
    "r-evaluate>=0.21"
    "r-jsonlite>=1.8.7"
    "r-lifecycle>=1.0.3"
    "r-magrittr>=2.0.3"
    "r-pkgload>=1.3.2.1"
    "r-praise>=1.0.0"
    "r-processx>=3.8.2"
    "r-ps>=1.7.5"
    "r-r6>=2.5.1"
    "r-rlang>=1.1.1"
    "r-waldo>=0.5.1"
    "r-withr>=2.5.0"
)
optdepends=(
    "r-covr"
    "r-curl>=0.9.5"
    "r-diffviewer>=0.1.0"
    "r-knitr"
    "r-rmarkdown"
    "r-rstudioapi"
    "r-shiny"
    "r-usethis"
    "r-vctrs>=0.1.0"
    "r-xml2"
)

# The unittests for `r-testthat` have multiple circular
# dependency chains (including itself!).

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-testthat`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("83be91814b5b4606a0581fd30153cd7c0189abf7634396243f5a639fde023de65a0ba742da4259bbd5062585638203fa61a2a92b13a007db3c1349c1f3585730")

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
