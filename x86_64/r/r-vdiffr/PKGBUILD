# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=vdiffr
_pkgver=1.0.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Visual Regression Testing and Graphical Diffing"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
        "fix-tests.patch"
        "$pkgname-skip_tests.patch::https://github.com/r-lib/vdiffr/commit/630a29d013361fd63fea242f531e2db6aef37919.patch")
md5sums=('392bc1fd9d13c621c5ad496e0548a828'
         'ba338395ac9bf4aeab0218b9ad262ce8'
         '2f12d37581d0e3af037a7066bdb9ee3b')
b2sums=('878556ae76d006a9a901373215f630ff7f644776f123acf3bf9d10c4c56d12c7cb518847a01df2c2ff53aac9a1029e4587714d5869669e9c1a76f3dce87a80ff'
        '3df04567ae9220dee53f3dc21ddca4d6ac2b06b39b32547ebde231c4af49146d7036069250357700d8ba95f39a7b0aa1657ee438027a6e8ac2b38266f1fe2c47'
        'cd2c66c4ab43fe0b34608a3de51fbed757b1c6e8607c9614d0dc600deb4bb9fb9d3b8798c58cae965c9674090360117ec5095feeed4503c71ae58dec83cddcd7')

prepare() {
  cd "$_pkgname"

  # revert a commit that disables all tests
  patch -Rp1 -i "../$pkgname-skip_tests.patch"

  # fix test snapshot
  sed -i 's/square/butt/' tests/testthat/_snaps/expect-doppelganger/myplot.svg

  # fix other snapshot tests
  patch -Np1 -i ../fix-tests.patch
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
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
