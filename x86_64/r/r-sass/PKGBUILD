# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sass
_pkgver=0.4.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Syntactically Awesome Style Sheets ('Sass')"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  libsass
  r-fs
  r-htmltools
  r-r6
  r-rappdirs
  r-rlang
)
checkdepends=(
  r-curl
  r-testthat
  r-withr
)
optdepends=(
  r-curl
  r-knitr
  r-rmarkdown
  r-shiny
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libsass.patch")
md5sums=('16054a7117a81ba75893fec17da62209'
         'e10e29d8d704275081d06953467928d5')
b2sums=('ffa2a4ffabea503c45d99cda26b62f75a5107e18caae6b40962901c090ac7031079b766f5556ca7815ca48438b7907cf537febe662be6682de39b9b55dd56805'
        '8c0b765fefe74d1e93abcc3d0249044431ec75ad26a9df83548720c07fd795f70e2117867032e05a742fd2ff7e844606aa210456968080052e9815d025a81f69')

prepare() {
  # build against system libsass
  patch -Np1 -i system-libsass.patch
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
