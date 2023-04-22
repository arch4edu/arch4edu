# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=dplyr
_cranver=1.1.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="A Grammar of Data Manipulation"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    r-cli
    r-generics
    r-glue
    r-lifecycle
    r-magrittr
    r-r6
    r-rlang
    r-tibble
    r-tidyselect
    r-vctrs
    r-pillar
)
optdepends=(
    r-bench
    r-broom
    r-callr
    r-covr
    r-dbi
    r-dbplyr
    r-ggplot2
    r-knitr
    r-lahman
    r-lobstr
    r-microbenchmark
    r-nycflights13
    r-purrr
    r-rmarkdown
    r-rmysql
    r-rpostgresql
    r-rsqlite
    r-stringi
    r-testthat
    r-tidyr
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('c220c38a3a44977c43eeae3d9aef90e8bb297150cad0993ea8d3cc13150096e3'
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
