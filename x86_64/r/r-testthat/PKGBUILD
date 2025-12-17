# Maintainer: Elio <ancibrothers@gmail.com>
# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_cranname=testthat
_cranver=3.3.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Unit Testing for R"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=4.1.0"
    "r-brio>=1.1.5"
    "r-callr>=3.7.6"
    "r-cli>=3.6.5"
    "r-desc>=1.4.3"
    "r-evaluate>=1.0.4"
    "r-jsonlite>=2.0.0"
    "r-lifecycle>=1.0.4"
    "r-magrittr>=2.0.3"
    "r-pkgload>=1.4.0"
    "r-praise>=1.0.0"
    "r-processx>=3.8.6"
    "r-ps>=1.9.1"
    "r-r6>=2.6.1"
    "r-rlang>=1.1.6"
    "r-waldo>=0.6.2"
    "r-withr>=3.0.2"
)
optdepends=(
    "r-covr"
    "r-curl>=0.9.5"
    "r-diffviewer>=0.1.0"
    "r-digest>=0.6.33"
    "r-knitr"
    "r-gh"
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

source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("76c29a6bd6f4323871c21fab5498f2b3a0776cdd4211cf05ca304c0afc3be0f6fc4d3b845e5a7eaa874d39558cb7184c38cb03ca29f3f1dfa222dc4ece5fdda8")

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
