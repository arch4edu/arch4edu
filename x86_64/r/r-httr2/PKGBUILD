# Maintainer: Alexander Bocken <alexander@bocken.org>

_cranname=httr2
_cranver=1.2.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Perform HTTP Requests and Process the Responses"
arch=('any')
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=('r>=3.4' 'r-cli>=3.0.0' 'r-curl>=6.4.0' 'r-glue' 'r-magrittr' 'r-lifecycle' 'r-openssl' 'r-r6' 'r-rappdirs' 'r-rlang>=1.1.0' 'r-vctrs>=0.6.3' 'r-withr')
optdepends=('r-askpass' 'r-bench' 'r-clipr' 'r-covr' 'r-docopt' 'r-httpuv' 'r-jose' 'r-jsonlite' 'r-knitr' 'r-purrr' 'r-rmarkdown' 'r-testthat>=3.1.8' 'r-tibble' 'r-webfakes' 'r-xml2')
source=(https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz)
sha256sums=(2728c37f5507740f41bde94703f74f67fc901ad122b1a58e8ad3af4224fd831e)

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
