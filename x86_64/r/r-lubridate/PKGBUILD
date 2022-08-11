# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Clint Valentine <valentine.clint@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_cranname=lubridate
_cranver=1.8.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=3
pkgdesc="Make Dealing with Dates a Little Easier"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(cctz r-generics)
makedepends=(r-cpp11)
checkdepends=(r-testthat)
optdepends=(
    r-covr
    r-knitr
    r-testthat
    r-vctrs
    r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('87d66efdb1f3d680db381d7e40a202d35645865a0542e2f270ef008a19002ba5')

prepare() {
  cd "${_cranname}"

  # skip snapshot test that is incompatible with r-vctrs 0.4.1
  sed -i '/"vctrs methods have informative errors"/a\ \ skip("Incompatible with vctrs>=0.4.1")' \
      tests/testthat/test-vctrs.R

  # skip test that requires a French locale
  sed -i '/"parsing months with dots works in French linux locale"/a skip("Requires a French locale")' \
      tests/testthat/test-parsers.R

  # build against system cctz
  sed -i -e 's|-I. -I./cctz/src/|-I.|' \
      -e 's/$(SHLIB): libcctz.a/$(SHLIB):/' \
      -e '/$(OBJECTS): libcctz.a/d' \
      src/Makevars
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
}

