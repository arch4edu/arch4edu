# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=pkgcache
_pkgver=2.2.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Cache 'CRAN'-Like Metadata and R Packages"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-callr
  r-cli
  r-curl
  r-filelock
  r-jsonlite
  r-processx
  r-r6
)
checkdepends=(
  r-mockery
  r-spelling
  r-testthat
  r-webfakes
)
optdepends=(
  r-covr
  r-debugme
  r-desc
  r-fs
  r-keyring
  r-pillar
  r-pingr
  r-rprojroot
  r-sessioninfo
  r-spelling
  r-testthat
  r-webfakes
  r-withr
  r-zip
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-bioc-fix.patch::https://github.com/r-lib/pkgcache/commit/8cefb54e030524bbcbb5885b2f0fe663f7932142.patch")
md5sums=('9f0b60ba5f78d69c38a5ba5b95748aae'
         'c31f9db16e6cc73b72672e739c549bdb')
b2sums=('2a45f9e01ca5ad9b80197364c89a222b0cb60dc68124aac9fc474e19b9c08c73be1d21e6c05cf44ebe28dc8188669380db80b383b29b84c5acc986e02ab2e881'
        '2b5deb4abc4cd55f355720a409397040b3d9191e5ab31f4b4367655f24d28afdd2f0235c43a6ac7f8b1d7a0973af8e8d35e415f061b959d1b75d2ee28cccad49')

#prepare() {
#  # fix bioc version mapping for tests
#  patch -Np1 -d "$_pkgname" < "$_pkgname-bioc-fix.patch"
#}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

#check() {
#  cd "$_pkgname/tests"
#  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
#}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
