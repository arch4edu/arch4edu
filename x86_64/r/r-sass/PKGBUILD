# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sass
_pkgver=0.4.9
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
md5sums=('7d4e8b37ce87b4307b6661b9fe62e393'
         '6a430d63f1fdeced20c3117763d2cb7c')
b2sums=('5d18e9430645ce11e0c19a6002538b96583493a12d4b7547b659855ff046505a8b71649ea68279017a0de94152037d6caaa65503e4df37d614ec5b2fe6377953'
        '8dce8f0d0eeff57916129505b0651115a1616431d0e4214a34b605ab89cefaee0d1e121e9a7db7709a880cd388f4c3305ade34e084938a413e32cffff46035e6')

prepare() {
  # build against system libsass
  patch -Np1 -i system-libsass.patch
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
