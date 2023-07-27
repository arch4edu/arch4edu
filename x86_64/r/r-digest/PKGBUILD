# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>
# Contributor: Grey Christoforo <first name at last name dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>
# Contributor: Francois Garillot <francois[@]garillot.net>

_pkgname=digest
_pkgver=0.6.33
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Create Compact Hash Digests of R Objects"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
md5sums=('f47359e9e90e279714c9fd50a47ad2ed')
sha256sums=('be702c886b1639be7eda4ea25a4261b30ce418c580f79bd78ec8d6cb4d327819')

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
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
