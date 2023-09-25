# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=vdiffr
_pkgver=1.0.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visual Regression Testing and Graphical Diffing"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
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
makedepends=(
  r-cpp11
)
checkdepends=(
  r-ggplot2
)
optdepends=(
  r-covr
  r-ggplot2
  r-roxygen2
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$pkgname-skip_tests.patch::https://github.com/r-lib/vdiffr/commit/630a29d013361fd63fea242f531e2db6aef37919.patch")
md5sums=('392bc1fd9d13c621c5ad496e0548a828'
         '2f12d37581d0e3af037a7066bdb9ee3b')
sha256sums=('ed432e5b67ee8b08e1aab5f7edb89da74e768da68ae6c6e2be483fcc354952d2'
            '66c843887b82cc78edd9300ef38140b19924a29c77e736897bef7520a5bb0d2f')

prepare() {
  cd "$_pkgname"

  # revert a commit that disables all tests
  patch -Rp1 -i "../$pkgname-skip_tests.patch"

  # fix test snapshot
  sed -i 's/square/butt/' tests/testthat/_snaps/expect-doppelganger/myplot.svg
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
