# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=glue
_cranver=1.6.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Interpreted String Literals"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r)
optdepends=(
    r-covr
    r-crayon
    r-dbi
    r-dplyr
    r-forcats
    r-ggplot2
    r-knitr
    r-magrittr
    r-microbenchmark
    r-r.utils
    r-rmarkdown
    r-rprintf
    r-rsqlite
    r-stringr
    r-testthat
    r-vctrs
    r-waldo
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('9da518f12be584c90e75fe8e07f711ee3f6fc0d03d817f72c25dc0f66499fdbf'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  install -Dm644 CRAN-MIT-TEMPLATE "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
