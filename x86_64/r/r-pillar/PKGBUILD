# Maintainer: Serene-Arc 
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=pillar
_cranver=1.11.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Coloured Formatting for Columns"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r"
    "r-cli>=2.3.0"
    "r-fansi"
    "r-glue"
    "r-lifecycle"
    "r-rlang>=1.0.2"
    "r-utf8>=1.1.0"
    "r-vctrs>=0.5.0"
)
optdepends=(
    "r-bit64"
    "r-dbi"
    "r-debugme"
    "r-diagrammer"
    "r-dplyr"
    "r-formattable"
    "r-ggplot2"
    "r-knitr"
    "r-lubridate"
    "r-nanotime"
    "r-nycflights13"
    "r-palmerpenguins"
    "r-rmarkdown"
    "r-scales"
    "r-stringi"
    "r-survival"
    "r-tibble"
    "r-units>=0.7.2"
    "r-vdiffr"
    "r-withr"
)

# The unittests for `r-pillar` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-pillar`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.1.1"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('7dc0bded54ea089086fdcbb0a9e5d9ca11e6cb25171a7c604df9c1dcfa37f947c81c453a43fcd75386f3fbff747d2936dd93d6348bfa0b5d90f8701575554a2d')

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
