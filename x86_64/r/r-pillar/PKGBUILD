# Maintainer: <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=pillar
_cranver=1.8.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Coloured Formatting for Columns"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    r
    "r-cli>=2.3.0"
    r-fansi
    r-glue
    r-lifecycle
    "r-rlang>=1.0.2"
    "r-utf8>=1.1.0"
    "r-vctrs>=0.3.8"
)
optdepends=(
    r-bit64
    r-debugme
    r-diagrammer
    r-dplyr
    r-formattable
    r-ggplot2
    r-knitr
    r-lubridate
    r-nanotime
    r-nycflights13
    r-palmerpenguins
    r-rmarkdown
    r-scales
    r-stringi
    r-survival
    "r-testthat>=3.1.1"
    r-tibble
    "r-units>=0.7.2"
    r-vdiffr
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=("52c6433692edede2731a95f58ae2bb4017fa50b62d3554c19b7c161d0a79b36f")

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
