# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sass
_pkgver=0.4.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Syntactically Awesome Style Sheets ('Sass')"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
md5sums=('c7ed9afd18a0e56ca42c7a21f49fb62c'
         '6a430d63f1fdeced20c3117763d2cb7c')
sha256sums=('717a08b63615a4fd9e494f775c33f0f965db83677cf1cc37849afc3da1c5e9ee'
            '5149aa34e5ab5ce03370495705e4162bbf1a3e7c7389be3ebe318c46d394eb10')

prepare() {
  # build against system libsass
  patch -Np1 -i system-libsass.patch
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
