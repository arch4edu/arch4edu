# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=xfun
_pkgver=0.41
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Supporting Functions for Packages Maintained by 'Yihui Xie'"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r
)
checkdepends=(
  r-testit
)
optdepends=(
  r-curl
  r-htmltools
  r-jsonlite
  r-knitr
  r-magick
  r-markdown
  r-mime
  r-pak
  r-remotes
  r-renv
  r-rhub
  r-rmarkdown
  r-rstudioapi
  r-testit
  r-tinytex
  r-yaml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('762d90da1dec41f701e35cd9450df7ef')
sha256sums=('2374c3b8f141f1e5ff01b291d8aa5c3dc807dd8e99ab4dc7a048c9534a7e3b02')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-cran.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
