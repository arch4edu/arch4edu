# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_cranname=testthat
_cranver=3.2.2
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
    "r-evaluate>=1.0.1"
    "r-jsonlite>=1.8.7"
    "r-lifecycle>=1.0.3"
    "r-magrittr>=2.0.3"
    "r-pkgload>=1.3.2.1"
    "r-praise>=1.0.0"
    "r-processx>=3.8.2"
    "r-ps>=1.7.5"
    "r-r6>=2.5.1"
    "r-rlang>=1.1.1"
    "r-waldo>=0.6.0"
    "r-withr>=3.0.2"
)
optdepends=(
    "r-covr"
    "r-curl>=0.9.5"
    "r-diffviewer>=0.1.0"
    "r-knitr"
    "r-rmarkdown"
    "r-rstudioapi"
    "r-s7"
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
b2sums=("10ec4de0db26f16aa99885b47ec27ca0bbc4535b073179e34c88388bbdeb261c167575b3792906239df116367dec2ec7cdd1a5c764f6f1c428653563e523fe3c")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     export R_LIBS="build/"
#     R CMD check --no-manual --ignore-vignettes "${_cranname}"
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
