# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=vdiffr
_cranver=1.0.5
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Visual Regression Testing and Graphical Diffing"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    libpng
    r-diffobj
    r-glue
    r-htmltools
    r-lifecycle
    r-rlang
    r-testthat
    r-xml2
)
makedepends=(r-cpp11)
checkdepends=(r-ggplot2)
optdepends=(
    r-covr
    r-ggplot2
    r-roxygen2
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "skip_tests.patch::https://github.com/r-lib/vdiffr/commit/630a29d013361fd63fea242f531e2db6aef37919.patch"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('0cbf7b72fcb7346a83a488c63b6b786fc2a4c5465093665ad2dee05396c4d0f0'
            '66c843887b82cc78edd9300ef38140b19924a29c77e736897bef7520a5bb0d2f'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

prepare() {
  cd "${_cranname}"

  # revert a commit that disables all tests
  patch -Rp1 -i "${srcdir}/skip_tests.patch"

  # fix test snapshot
  sed -i 's/square/butt/' tests/testthat/_snaps/expect-doppelganger/myplot.svg
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
