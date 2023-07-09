# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_cranname=testthat
_cranver=3.1.10
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Unit Testing for R"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=3.1"
    "r-brio"
    "r-callr>=3.5.1"
    "r-cli>=3.4.0"
    "r-desc"
    "r-digest"
    "r-ellipsis>=0.2.0"
    "r-evaluate"
    "r-jsonlite"
    "r-lifecycle"
    "r-magrittr"
    "r-pkgload>=1.3.0"
    "r-praise"
    "r-processx>=3.8.2"
    "r-ps>=1.3.4"
    "r-r6>=2.2.0"
    "r-rlang>=1.0.1"
    "r-waldo>=0.5.0"
    "r-withr>=2.4.3"
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
# dependency chains.

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
b2sums=("9fcdfb2119f5446815cd3a03c849a87be0e1048d54bb360db45d94b431f2b64469595bcfe9077379700c7675f300a93f744ef445598699ca774b7f513b78a1a3")

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
