# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=parallelly
_pkgver=1.41.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Enhancing the 'parallel' Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r
)
optdepends=(
  r-base64enc
  r-commonmark
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b9a231b2145990d97968aee7ac27f901')
b2sums=('7667cb673ed296e42fe93b3774f9cdd3828d93586a9b9e0b6c112be4dcea5ce2103d82d2968568dbf1a615554af0c89d046745b58ab33be5c066665c9a263c43')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
