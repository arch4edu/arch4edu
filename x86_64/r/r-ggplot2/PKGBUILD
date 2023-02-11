# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_cranname=ggplot2
_cranver=3.4.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Create Elegant Data Visualisations Using the Grammar of Graphics"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    r-cli
    r-glue
    r-gtable
    r-isoband
    r-lifecycle
    r-rlang
    r-scales
    r-tibble
    r-vctrs
    r-withr
)
checkdepends=(
    r-hexbin
    r-mapproj
    r-quantreg
    r-sf
    r-sp
    r-svglite
    r-testthat
    r-xml2
    ttf-font
)
optdepends=(
    r-covr
    r-ragg
    r-dplyr
    r-ggplot2movies
    r-hexbin
    r-hmisc
    r-knitr
    r-mapproj
    r-maps
    r-maptools
    r-multcomp
    r-munsell
    r-profvis
    r-quantreg
    r-rcolorbrewer
    r-rgeos
    r-rmarkdown
    r-sf
    r-svglite
    r-testthat
    r-vdiffr
    r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('041bc333f90d6026702c8bd5140a1c8ddd270b15742badf8ca5c53f0e02c6d84'
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

  install -Dm644 CRAN-MIT-TEMPLATE "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
