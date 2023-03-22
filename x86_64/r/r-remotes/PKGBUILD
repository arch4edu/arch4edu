# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=remotes
_cranver=2.4.2
pkgname=r-${_cranname,,}
pkgdesc="R package installation from remote repositories, including GitHub"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=2

arch=("any")
depends=(
    "r>=3.0.0"
)
optdepends=(
    "r-brew"
    "r-callr"
    "r-codetools"
    "r-curl"
    "r-covr"
    "r-git2r>=0.23.0"
    "r-knitr"
    "r-mockery"
    "r-pkgbuild>=1.0.1"
    "r-pingr"
    "r-rmarkdown"
    "r-rprojroot"
    "r-testthat"
    "r-webfakes"
    "r-withr"
)
checkdepends=(
    "${optdepends[@]}"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("f189cbdd6d687145a031f6e3e267e68db891f526e61acf16e93c7af3aa1af8fbffb713d8b00af9d9ad52c4dd1fedad72fed528b319f996ef6b0060ebf607102d")

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

check() {
    cd "${srcdir}/${_cranname}/tests"
    R_LIBS="${srcdir}/build/" Rscript --vanilla testthat.R
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
