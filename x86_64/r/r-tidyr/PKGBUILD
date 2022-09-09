# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=tidyr
_cranver=1.2.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Tidy Messy Data"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    r-dplyr
    r-ellipsis
    r-glue
    r-lifecycle
    r-magrittr
    r-purrr
    r-rlang
    r-tibble
    r-tidyselect
    r-vctrs
)
makedepends=(r-cpp11)
checkdepends=(r-data.table r-testthat)
optdepends=(
    r-covr
    r-data.table
    r-jsonlite
    r-knitr
    r-readr
    r-repurrrsive
    r-rmarkdown
    r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('6971766d3663dc75c2328ab257816f4e42d9fdc05c2d87d171b8b9b5ecce61af'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

prepare() {
  cd "${_cranname}/tests/testthat"

  # Skip outdated snapshot tests
  sed -i '/"errors are raised"/a\ \ skip("Outdated snapshot")' test-drop-na.R
  sed -i '/must be supplied/a\ \ skip("Outdated snapshot")' test-pivot-wide.R
}

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  install -Dm644 CRAN-MIT-TEMPLATE "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
