# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=vctrs
_cranver=0.5.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Vector Helpers"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=3.3"
    "r-cli>=3.4.0"
    "r-glue"
    "r-lifecycle>=1.0.3"
    "r-rlang>=1.0.6"
)
optdepends=(
  "r-bit64"
  "r-covr"
  "r-crayon"
  "r-dplyr>=0.8.5"
  "r-generics"
  "r-knitr"
  "r-pillar>=1.4.4"
  "r-pkgdown>=2.0.1"
  "r-rmarkdown"
  "r-testthat>=3.0.0"
  "r-tibble>=3.1.3"
  "r-withr"
  "r-xml2"
  "r-waldo>=0.2.0"
  "r-zeallot"
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("e5575c957f508aeb3ffed9e160b93c7296ed38765da175672d0021f3258034e0219c7c7b9b0ecd466474d43ae092483cc8415e2bf368235c1a7cbb6c6ff2637e")

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
