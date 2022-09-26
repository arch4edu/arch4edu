# Maintainer: <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=rlang
_cranver=1.0.6
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Functions for Base Types and Core R and 'Tidyverse' Features"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=("r>=3.4.0")
optdepends=(
    "r-cli>=3.1.0"
    r-covr
    r-crayon
    r-fs
    r-glue
    r-knitr
    r-magrittr
    r-pillar
    r-rmarkdown
    "r-testthat>=3.0.0"
    r-tibble
    r-usethis
    "r-vctrs>=0.2.3"
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=("e6973d98a0ea301c0da1eeaa435e9e65d1c3f0b95ed68bdc2d6cb0c610166760")

build() {
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"

    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
