# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=tidyselect
_cranver=1.2.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Select from a Set of Strings"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    r-cli
    r-glue
    r-lifecycle
    r-rlang
    r-vctrs
    r-withr
)
checkdepends=(r-stringr r-testthat)
optdepends=(
    r-covr
    r-crayon
    r-dplyr
    r-knitr
    r-magrittr
    r-rmarkdown
    r-stringr
    r-testthat
    r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('538d26b727e37d618e2efd3b00836048f103112a03e6994bf07a02392e269e3b'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

prepare() {
  cd "${_cranname}/tests/testthat"

  # skip outdated snapshot tests
  sed -i '/"all_of() and any_of() check their inputs"/a\ \ skip("outdated snapshot")' \
      test-helpers-vector.R
  sed -i -e '/"vars_select() type-checks inputs"/a\ \ skip("outdated snapshot")' \
      -e '/"vars_rename() type-checks arguments"/a\ \ skip("outdated snapshot")' \
      test-lifecycle-deprecated.R
  sed -i '/"errors for bad inputs"/a\ \ skip("outdated snapshot")' \
      test-vars-pull.R
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
