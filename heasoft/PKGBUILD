# Maintainer:  Yigit Dallilar <yigit.dallilar@gmail.com>
# 
# for _mod use either (src_no_xspec_modeldata or src) and dont forget to change sha256sums

pkgname=heasoft
pkgver=6.26.1
pkgrel=1
_mod="src_no_xspec_modeldata" 
pkgdesc="NASA high energy astrophysics library"
makedepends=("gcc" "glibc" "gcc-fortran" "perl")
depends=("ncurses" "readline" "libxpm" )
url="https://heasarc.gsfc.nasa.gov/docs/software/lheasoft/"
arch=('x86_64')
license=('NASA' 'GPL')
source=(https://heasarc.gsfc.nasa.gov/FTP/software/lheasoft/lheasoft${pkgver}/${pkgname}-${pkgver}${_mod}.tar.gz)
sha256sums=('2bffdbc2a02f3bc69ab59a8ff881c75abe83d3064dc59bf8be261d638cd1afe0')
install="${pkgname}.install"

build() {

  export CC=/usr/bin/gcc
  export CXX=/usr/bin/g++
  export FC=/usr/bin/gfortran
  export PERL=/usr/bin/perl

  cd $srcdir/${pkgname}-${pkgver}/BUILD_DIR
  ./configure --prefix=${pkgdir}/opt/${pkgname}
  
  make 

}

package(){

  cd $srcdir/${pkgname}-${pkgver}/BUILD_DIR
  make install


  #mkdir -p $pkgdir/opt/${pkgname}-${pkgver}/x86_64-unknown-linux-gnu-libc${_glibcver}/bin/

 
}

