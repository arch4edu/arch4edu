# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sass
_pkgver=0.4.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('fb188e1129cca127e7790ffccff4e1f7'
         '6a430d63f1fdeced20c3117763d2cb7c')
sha256sums=('2ee82ce709b7fdee78f7e2364d04f369f58fc2cda4bb5a235bd53c49d311c019'
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
