# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=zip
_pkgver=2.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Cross-Platform 'zip' Compression"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(MIT)
depends=(
  r
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-processx
  r-r6
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "libr-zip.patch")
md5sums=('4f4294028c8902df55475b69a249c06c'
         '66828a1ae6c6d7bb94b97864f6b57029')
b2sums=('c2a0b41370f73b42d24101d53077f48bb818637e1bdb2da1b4ad11b2c0284ed21784144ed35248a397d951b45419b1911cb7b89c27a9b0f04c06bfaafc55f9de'
        'bd8012554ac72052ca748acc8990a20d685788fc03ff17036fa83f7ec3c82a63026f567bd1c84ae0980213d82ed2c93211de299cd9657d59e2cff8a9b69fc7f2')

prepare() {
  # fix LDFLAGS, put common functionality into libr-zip.so
  patch -Np1 -i libr-zip.patch
}

build() {
  mkdir build
  # set LD_LIBRARY_PATH for libr-zip.so
  LD_LIBRARY_PATH="$srcdir/$_pkgname/src" R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  LD_LIBRARY_PATH="$srcdir/$_pkgname/src" R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"

  # move libr-zip.so to /usr/lib
  mv "$pkgdir/usr/lib/R/library/$_pkgname/libs/libr-zip.so" "$pkgdir/usr/lib"
}
