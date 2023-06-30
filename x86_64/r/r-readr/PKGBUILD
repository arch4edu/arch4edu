# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=readr
pkgname=r-${_cranname,,}
pkgver=2.1.4
_cranver=${pkgver}
pkgrel=1
pkgdesc="Read Rectangular Text Data"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=('r>=3.1' r-cli r-clipr r-crayon 'r-hms>=0.4.1' r-rlang r-r6 r-tibble 'r-vroom>=1.5.6' 'r-lifecycle>=0.2.0' r-cpp11 'r-tzdb>=0.1.1')
optdepends=(r-covr r-curl r-knitr r-rmarkdown r-spelling r-stringi r-testthat r-tzdb r-waldo r-withr r-xml2)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('98144fa48c4fa61ef8c73ede8f87a2d2c5c44e9502b7875b266eb79984fbeb0d')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
