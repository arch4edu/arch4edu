# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=StanHeaders
_pkgver=2.32.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="C++ Header Files for Stan"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r-rcppparallel
)
makedepends=(
  gcc-fortran
  r-rcppeigen
)
optdepends=(
  r-bh
  r-knitr
  r-rcpp
  r-rmarkdown
  r-rstan
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-flags.patch")
md5sums=('9132b500cd1a8119b40eacfaa603055b'
         '0d0c50619b42dc9d75209fc43320c71b')
b2sums=('0d4f074e70e08c27da4525afbfe2b32e5726edfe9ecda0a59a53a2586f62f341decc93b3d7e000cf5f6c0968d7125f916c93af1772b395f8dac777e6e24475ce'
        '11ef9d240340ee8aaee7d0786dfbd8b412c90b22289a4fc1b9787907b78c6fd75a401078f1be796833fbc87f18095a0960c1b132efc2481e339a10bccf8782aa')

prepare() {
  # fix onetbb build flags
  patch -Np1 -i fix-flags.patch
}

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
