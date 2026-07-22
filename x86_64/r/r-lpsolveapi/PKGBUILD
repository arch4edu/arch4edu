# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lpSolveAPI
_pkgver=5.5.2.0-17.15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="R Interface to 'lp_solve' Version 5.5.2.0"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.0-only')
depends=(
  lpsolve
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libs.patch")
md5sums=('70ff8cb98049cc5cffcf99a2691fd26d'
         'b05adde5cc4292eea42da677062a3c57')
b2sums=('f30df52f0a909d4b4723277ff60951350c147b96484afacf5ea35ae73bdb711db8a9a4557011862a554f7aa24b06e6ed99472ee586a106b3aa08a686cd66b885'
        'b50c98ff88ad664a9cad84c1ea8d8a277d193845b0677566d14d6b8b82522d15667c5b97e70ae1244d2ecd06a9691e924393c4d23da189bfb01224c81f0b7ed8')

prepare() {
  # use system lpsolve
  patch -Np1 -i system-libs.patch
  cd "$_pkgname"
  # rename type REAL to LPSREAL in lpsolve headers, since R headers have a conflicting definition
  cp -r /usr/include/lpsolve src/include
  sed -i 's/REAL/LPSREAL/g' -- src/include/*.h
  mv inst/include/RlpSolve{,Link}.h src/include/
  # remove the unnecessary header files so that they don't get installed
  rm -r inst/include
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla lpSolveAPI.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
