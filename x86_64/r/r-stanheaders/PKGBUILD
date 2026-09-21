# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=StanHeaders
_pkgver=2.39.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('e0875d728217e5b33ff17700c2717c3e'
         'fe22ab5369c21c8018635c2d61308830')
b2sums=('53f022bf0df4faf55846f4b1072b6ffeac631882a0623718f61a1876df55bd5bec671c99ed4bb76ed275a9abddfc9e700fe8141d7ce7e55c6754fb0dad619da6'
        '67c49e39f6445bb8335684d92c115d2295d46af8404abe344ef5a5dd027c007520cf69603392f5984a8d2bf25fa611462849260b4540d83f1b83fe8187204b4a')

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
