# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_cranname=testthat
_cranver=3.1.7
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
    "r-pkgload"
    "r-praise"
    "r-processx"
    "r-ps>=1.3.4"
    "r-r6>=2.2.0"
    "r-rlang>=1.0.1"
    "r-waldo>=0.4.0"
    "r-withr>=2.4.3"
)
optdepends=(
    "r-covr"
    "r-curl>=0.9.5"
    "r-diffviewer>=0.1.0"
    "r-knitr"
    "r-mockery"
    "r-rmarkdown"
    "r-rstudioapi"
    "r-shiny"
    "r-usethis"
    "r-vctrs>=0.1.0"
    "r-xml2"
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('aed7c006139c6193408ae02cd28037909313497e7e5cd14706507f4ddfe8632d73b2e3c8d88fd626001bf3fc6fbc42b711b7b10470976c3519fb1a4af8e5b730')

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
