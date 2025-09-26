# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ragg
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Graphic Devices Based on AGG"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  freetype2
  libjpeg-turbo
  libpng
  libtiff
  r-systemfonts
  r-textshaping
)
checkdepends=(
  r-testthat
  ttf-font
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fa47937c6bd1b495fa6d7d3d3c41694a')
b2sums=('39473f7802610d7c308212c65853eebd789d38c6cb4d65ba9c022357f01f2bfda1dc4a6565be8dd63ff51f470c34b7da30bad48a7a6f6ef1e6ad5aafbbfd2fcd')

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
