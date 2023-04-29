# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=xml2
_cranver=1.3.4
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Parse XML"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r libxml2)
checkdepends=(r-mockery r-testthat)
optdepends=(
    r-covr
    r-curl
    r-httr
    r-knitr
    r-magrittr
    r-mockery
    r-rmarkdown
    r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('340bb1a18e643a5008c0b4e92d71c3b0abacb44f1742e3a77d0cb33cb73b3030')

build() {
  mkdir -p build
  R CMD INSTALL "$_cranname" -l build
}

check() {
  cd "$_cranname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_cranname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_cranname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
