# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=sass
_cranver=0.4.6
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Syntactically Awesome Style Sheets ('Sass')"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    libsass
    r-fs
    r-rlang
    r-htmltools
    r-r6
    r-rappdirs
)
checkdepends=(r-curl r-testthat r-withr)
optdepends=(
    r-testthat
    r-knitr
    r-rmarkdown
    r-withr
    r-shiny
    r-curl
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('2ee82ce709b7fdee78f7e2364d04f369f58fc2cda4bb5a235bd53c49d311c019')

prepare() {
  # build against system libsass
  sed -e 's|PKG_LIBS = ./libsass/lib/libsass.a|PKG_LIBS = -lsass|' \
      -e '/PKG_CPPFLAGS = -I/d' \
      -e 's|$(SHLIB): libsass/lib/libsass.a|$(SHLIB):|' \
      -i "$_cranname/src/Makevars"
}

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
