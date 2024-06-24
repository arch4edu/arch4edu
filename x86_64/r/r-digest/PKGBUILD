# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: Grey Christoforo <first name at last name dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>
# Contributor: Francois Garillot <francois[@]garillot.net>

_pkgname=digest
_pkgver=0.6.36
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Create Compact Hash Digests of R Objects"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  google-crc32c
  libblake3
  r
  xxhash
  zlib
)
checkdepends=(
  r-tinytest
)
optdepends=(
  r-simplermarkdown
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c7cf622332bd8f3a5c967d05bc962598')
b2sums=('c54ae640d8e1771cddd37d1c4b6a6b6322fc85c574a6359e85ad474ab79ceae654b3b93dd83fff7ad39c1c71da6f876a2c7f38f83009dce35d8327ac81cc1d29')

prepare() {
  cd "$_pkgname/src"
  # use system blake3, crc32c, xxhash and zlib
  rm -r crc32c
  rm blake3* crc32.* crc32c* xxhash.* z*
  sed -i 's/digest_crc32/crc32/' digest.c
  sed -e 's|PKG_CPPFLAGS = -I.|PKG_CPPFLAGS = -I/usr/include/crc32c -I.|' \
      -e '2 a PKG_LIBS = -lblake3 -lcrc32c -lxxhash -lz' \
      -i Makevars
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
