# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributorr: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=modeltools
_pkgver=0.2-25
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools and Classes for Statistical Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1beb2a6b9a2cf032488082a33d136c2b')
b2sums=('6a6c2ed8eff9d92b450cf732de92b8e6c10e1779d9f156173017c915f418ecf393f93668451a09f6cc0774345a1bead368a1a4c2f17a05da7a1a9e171956e531')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
