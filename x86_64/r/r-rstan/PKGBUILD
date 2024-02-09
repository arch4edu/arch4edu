# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=rstan
_pkgver=2.32.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="R Interface to Stan"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  onetbb
  pandoc
  r-ggplot2
  r-gridextra
  r-inline
  r-loo
  r-pkgbuild
  r-quickjsr
  r-rcpp
  r-rcppparallel
  r-stanheaders
)
makedepends=(
  r-bh
  r-rcppeigen
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-bayesplot
  r-coda
  r-knitr
  r-rmarkdown
  r-rstantools
  r-rstudioapi
  r-shinystan
  r-testthat
  r-v8
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-plugin.patch")
md5sums=('0d7ea5114187f589f6a2255cf1eeb397'
         '4bd2cd1d41029fb5d9b792b56d9cd524')
b2sums=('509272c2b88ad2d1949620fc5ad7a32ab894005a829226ec9ccf39af0cd7bbbcfc4faee798f75ba4f4a984a827bae491cbdc52b7ea1c9292054382dae02bc3d9'
        'b5cb53f8d2e3cc84ebbed12e8439f59f5b1b62b747a3e6f9212750b882ee2833319af69cd973734670fba7bdbd924bc5a2d63733c60ddf437623bc83d3f3e4a7')

prepare() {
  # fix Rcpp plugin to use system onetbb
  patch -Np1 -i fix-plugin.patch
}

build() {
  mkdir build
  TZ=UTC R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  TZ=UTC R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
