# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=markdown
_cranver=1.7
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Render Markdown with 'commonmark'"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r-commonmark r-xfun)
optdepends=(
    r-knitr
    r-rmarkdown
    r-yaml
    r-rcurl
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('cb2b9a4752174406b3b3557b0da943ab37041e6b1d993281d59614bb2acdcfb1')

build() {
  mkdir -p build
  R CMD INSTALL "$_cranname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_cranname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_cranname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
