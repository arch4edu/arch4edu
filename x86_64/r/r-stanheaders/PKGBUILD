# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=StanHeaders
_pkgver=2.32.6
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
md5sums=('6186e76365d883342e98effa1176b3f3'
         '0d0c50619b42dc9d75209fc43320c71b')
b2sums=('5864e8df45e52056264ac607166234fabf20a97ee6e4bf423d2c51e3faeec8d0b91b7758a79c846275ce70a211b72b98c65fa0f784a7b2ba6011b43a720bda7f'
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
