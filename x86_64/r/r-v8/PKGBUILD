# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=V8
_pkgver=8.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Embedded JavaScript and WebAssembly Engine for R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  libnode
  r-curl
  r-jsonlite
  r-rcpp
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6cae314842087ce6253117501f73a1ee')
b2sums=('9e65b482cb279354028fb83aee0614fd06f411165373727c46286ee01c50ed01ec2f4f61ec27d70e1120cd6d235dc2c10f358030a0f3a5844c08a0bb5cb1cc92')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname" \
      --configure-vars="V8_PKG_LIBS=-lnode V8_PKG_CFLAGS=-I/usr/include/libnode"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
