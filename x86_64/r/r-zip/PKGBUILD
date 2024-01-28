# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=zip
_pkgver=2.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Cross-Platform 'zip' Compression"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
md5sums=('8a8a132cd0456e498d479d21c91facce'
         '54567d238fb1409ea2a6fcd82034b15b')
b2sums=('dc1334e069693b47d45887319bd3f446d2582476c0d24d0eb31465de5df1bdb28272b538d68dafd844ecd7ea96ca27481c00cf613bbec19d1ef0641255aa706c'
        '9f00d0cae1521ffc8831e0c2261e8a88f9a255d01fedb5d0f0f2f6e82c6c30834d0c21130e51d131c9414c058f35d640ac50affdb312a7c3255e40c85b85b181')

prepare() {
  # fix LDFLAGS, put common functionality into libr-zip.so
  patch -Np1 -i libr-zip.patch
  # rename miniz symbols with r_ prefix, see https://github.com/r-lib/zip/issues/98
  cd "$_pkgname/src"
  sed -i 's/mz_/r_mz_/g' *.c *.h
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
