# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=vctrs
_cranver=0.6.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Vector Helpers"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    "r>=3.5.0"
    "r-cli>=3.4.0"
    "r-glue"
    "r-lifecycle>=1.0.3"
    "r-rlang>=1.1.0"
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
b2sums=("beb61d84ed85b5b9ea11da1d95e5a2b7debde033d8ce3c528fcd64d1639769f22a0fffabba3860411b925ffe253e3a285c4248c862d0cac13d85ba4d75663976")

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
