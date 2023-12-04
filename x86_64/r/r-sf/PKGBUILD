# Maintainer: peippo <christoph+aur@christophfink.com>

_cranname=sf
_cranver=1.0-14
pkgname=r-${_cranname,,}
pkgdesc="Simple Features for R"
url="https://cran.r-project.org/package=sf"
license=("GPL-2 | MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=3

arch=("i686" "x86_64")
depends=(
    "gdal>=2.0.1"
    "geos>=3.4.0"
    "proj>=4.8.0"
    "r>=3.3.0"
    "r-classint>=0.4.1"
    "r-dbi>=0.8"
    "r-magrittr"
    "r-rcpp>=0.12.18"
    "r-s2>=1.1.0"
    "r-units>=0.7.0"
    "sqlite"
)
optdepends=(
    "r-blob"
    "r-covr"
    "r-dplyr>=0.8.3"
    "r-ggplot2"
    "r-knitr"
    "r-lwgeom>=0.2.1"
    "r-maps"
    #"r-mapview"
    "r-matrix"
    "r-microbenchmark"
    "r-odbc"
    "r-pbapply"
    "r-pillar"
    "r-raster"
    "r-rlang"
    "r-rmarkdown"
    "r-rpostgres>=1.1.0"
    "r-rpostgresql"
    "r-rsqlite"
    "r-sp>=1.2.4"
    "r-spatstat>2.0.1"
    "r-spatstat.geom"
    "r-spatstat.linnet"
    "r-spatstat.random"
    "r-spatstat.utils"
    "r-stars>=0.2.0"
    "r-terra"
    "r-tibble>=1.4.1"
    "r-tidyr>=1.2.0"
    "r-tidyselect>=1.0.0"
    #"r-tmap"
    "r-vctrs"
    "r-wk"
)

# The unittests for `r-sf` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-sf`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.0.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("0d501b4cee1a457cf1e1eeb3f498077bc54503b854fab4088ea439db961724ceb0f96e921819631c3c37acc7da5978f2b5a3247c9a34b047fe04d33f5d45d27a")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

# check() {
#     export R_LIBS="build/"
#     export _R_CHECK_FORCE_SUGGESTS_=0
#     R CMD check --no-manual "${_cranname}"
# }

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
