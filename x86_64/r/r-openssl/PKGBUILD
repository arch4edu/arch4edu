# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=openssl
_pkgver=2.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Toolkit for Encryption, Signatures and Certificates Based on OpenSSL"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  openssl
  r-askpass
)
checkdepends=(
  r-curl
  r-sodium
  r-testthat
)
optdepends=(
  r-curl
  r-digest
  r-jose
  r-jsonlite
  r-knitr
  r-rmarkdown
  r-sodium
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4c90a780fe0e9d65448a28a06568dbd0')
b2sums=('b181a881ed47c180c1c0c40862e65fc2e7de14e7fab8994ae43c024fe463e1653826ab2146ad9175e075d91a3c379f91c58862713966dc73e0d7da623441f24f')

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
