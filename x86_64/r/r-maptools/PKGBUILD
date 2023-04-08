# Maintainer: Danilo J. S. Bellini <danilo dot bellini at gmail dot com>
_cranname=maptools
_cranver=1.1
_cranrel=6
pkgname="r-$_cranname"
pkgver="${_cranver}_$_cranrel"
pkgrel=1
pkgdesc="Tools for Reading and Handling Spatial Objects"
arch=('x86_64')
_cranurl=http://cran.r-project.org
url="$_cranurl/web/packages/$_cranname/index.html"
license=('GPL')
depends=('r' 'r-sp')
options=(!emptydirs)
sha256sums=('d6a5df52db03b2231f21921b693c67f85df3c3b376181aa13ef4f21710f69308')
source=("$_cranurl/src/contrib/${_cranname}_${_cranver}-$_cranrel.tar.gz")

package() {
  cd "$srcdir"
  mkdir -p "$pkgdir/usr/lib/R/library"
  R CMD INSTALL "$_cranname/" -l "$pkgdir/usr/lib/R/library"
}
