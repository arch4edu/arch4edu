# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=shinyjs
_cranver=2.1.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Easily Improve the User Experience of Your Shiny Apps in Seconds"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r-digest r-jsonlite r-shiny)
checkdepends=(r-testthat)
optdepends=(
    r-htmltools
    r-knitr
    r-rmarkdown
    r-shinyace
    r-shinydisconnect
    r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "R-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('7ec20cbf1b1fd7a32d85a56dfc0df8b5f67c828d241da400a21d893cb37ea9c5'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

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

  install -Dm644 R-MIT-TEMPLATE "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
