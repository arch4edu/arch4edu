# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=pkgload
_cranver=1.3.4
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Simulate Package Installation and Attach"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(
    "r>=3.4.0"
    "r-cli>=3.3.0"
    "r-crayon"
    "r-desc"
    "r-fs"
    "r-glue"
    "r-pkgbuild"
    "r-rlang>=1.0.3"
    "r-rprojroot"
    "r-withr>=2.4.3"
)
optdepends=(
    "r-bitops"
    "r-covr"
    "r-mathjaxr"
    "r-mockr"
    "r-pak"
    "r-rcpp"
    "r-remotes"
    "r-rstudioapi"
)

# The unittests for `r-pkgload` have multiple circular
# dependency chains.

# As such, the tests can not be run on first build.
# While R packages from CRAN, generally, are well-tested
# before they are released, in some situations, you want to
# have thorough testing on your own end.

# To run the tests, first build this package without `check()`
# (i.e., as-is) to bootstrap `r-pkgload`. Then, on subsequent builds,
# (assumining you have a local repository that is accessible from
# the build chroot), uncomment the lines defining `checkdepends`, below,
# as well as the `check()` function further down

# checkdepends=(
#     "${optdepends[@]}"
#     "r-testthat>=3.1.0"
# )

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("ac2fdc0d429ef5be97b24b984646acad2dc9def5447713ee9689070f2a54228dd3f353a24a307d24c12ec72021e91db0bc033ca1ee8c15b0d5ef7c1fa4aa8900")

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
