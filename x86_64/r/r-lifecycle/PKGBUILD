# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=lifecycle
_cranver=1.0.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Manage the Life Cycle of your Package Functions"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=('r>=3.3' r-glue 'r-rlang>=0.4.10')
optdepends=(r-covr r-crayon r-lintr r-tidyverse r-knitr r-rmarkdown r-testthat r-tibble r-vctrs)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('1da76e1c00f1be96ca34e122ae611259430bf99d6a1b999fdef70c00c30f7ba0')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
