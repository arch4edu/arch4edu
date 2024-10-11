# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=evaluate
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Parsing and Evaluation Tools that Provide More Details than the Default"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-covr
  r-ggplot2
  r-rlang
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a57f0d289e7fda95bfaa4ebe8836af05')
b2sums=('e35853ce5a3621e8dfe962a4dc4a5fe57338b3933786cad1ff895561b38da264b353b030d0a5ef75b16fed4d994648cddc18b1c0328373f42414746c357eb69a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
