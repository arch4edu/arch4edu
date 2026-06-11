# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=timechange
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Efficient Manipulation of Date-Times"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  cctz
  r
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-cctz.patch")
md5sums=('4cabacecbed68e3beb00e47d42fc9fca'
         '0111def4195dc0497273ed1c287e1906')
b2sums=('d037c1d8872583fe33b8f36b86d33ddac29fbb95114a6717e9dcb510d0be0595cb60ac1cbd75a04e08e62d1a907a8ab71e07b31c9b71fce4640902e3d10ed1ac'
        'b3178081cb18390b88fc540fe5ea29393336b03bb51b582c281c5dee371d7b419f3dec7acd02f850f853bad3fc2bbe2173eb9c8526a28abde5d030f7b95feb15')

prepare() {
  # build against system cctz
  patch -Np1 -i system-cctz.patch
}

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
}
