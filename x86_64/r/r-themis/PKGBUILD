# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=themis
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Extra Recipes Steps for Dealing with Unbalanced Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-dplyr
  r-generics
  r-glue
  r-gower
  r-hardhat
  r-lifecycle
  r-purrr
  r-rann
  r-recipes
  r-rlang
  r-rose
  r-tibble
  r-vctrs
  r-withr
)
checkdepends=(
  r-dials
  r-modeldata
  r-testthat
)
optdepends=(
  r-covr
  r-dials
  r-ggplot2
  r-modeldata
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-update-snapshots-1.patch::https://github.com/tidymodels/themis/commit/c9bdc843f3c299e668f1b41dee1d1f11deceb4ba.patch"
        "$_pkgname-update-snapshots-2.patch::https://github.com/tidymodels/themis/pull/147.patch")
md5sums=('8f13545a8a8d475f3323e75dd40a66d3'
         '20778cbb20ffa0fd16e18b24e0471915'
         'c23888ea75a5b79aedee4fc2993569e4')
b2sums=('10e3a4edea7c0d48af8d133c5f6cc435782daeb16b4978c835884d9ed4126baa9a12aeabba0f3f9986598c14df2151ed907a4095478ab192990bc018d05fab7a'
        '127214d54c11d26fba58f0f6e66fd0bf9cb876533a38aaf5d332a75baea9b4b4f1ff3924460c883a6303eb241bcbeee95d762df938101c879b696be5d806f347'
        '63d251544560c1d67e5dd2b39d9e25fc8bc05e6db84c2609fa75850e9e5148d949986fd1afb2065f5ccfc9f9b782a3d0ae82460eaa9bf106bd96a04765dde0a8')

prepare() {
  cd "$_pkgname"
  # fix test snapshots
  patch -Np1 -i "../$_pkgname-update-snapshots-1.patch"
  patch -Np1 -i "../$_pkgname-update-snapshots-2.patch"
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
