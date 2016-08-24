# Contributor: Oliver Bandel <oliver@first.in-berlin.de>
# Derived from the 32-bit version PKGBUILD (J. Lichtblau and T. Adams)

pkgname=htk
pkgver=3.4.1
pkgrel=3
pkgdesc="A portable toolkit primarily used for speech recognition research"
arch=('x86_64')
#arch=('i686')
url="http://htk.eng.cam.ac.uk/"
license=('custom: Proprietary')
depends=('lib32-glibc' 'lib32-libx11')
makedepends=('wget' 'gcc-multilib')
options=('!makeflags')
#source=(http://htk.eng.cam.ac.uk/ftp/software/HTK-$pkgver.tar.gz)
source=(mkfile.in.patch)
#md5sums=('b3fc12006b0af12f59cd573c07aa4c1d')
md5sums=('10eec9a139acea719c0b9f451d8f7807')

build() {

# Note: HTK cannot be downloaded without a username/password. Use name and password from your registration here.
# http://htk.eng.cam.ac.uk/ftp/software/HTK-3.4.1.tar.gz
#  wget --user=YOUR_USERNAME --password=YOUR_PASSWORD http://htk.eng.cam.ac.uk/ftp/software/HTK-$pkgver.tar.gz

  # unpack file
  tar -xzvf HTK-$pkgver.tar.gz

  #mv htk ${pkgname}   # needed before, as pkgname was "pkg64"
  # here now 64-bit-optimization might be introduced...
  if  [ "$HOSTTYPE" == "x86_64" ];
  then
    echo 64 Bit
  else
    echo 32 Bit
  fi

set | grep -e 32 -e 64
#exit
  # substitute spaces instead of tabs in Makefile-rule
  patch  ${srcdir}/${pkgname}/HLMTools/Makefile.in ../mkfile.in.patch


  # make the stuff
  cd ${srcdir}/${pkgname}
  ./configure --prefix=${pkgdir}/usr
  make all
}

package() {
  # create a needed dir
  mkdir -p ${pkgdir}/usr/bin

  # install binaries
  cd ${srcdir}/${pkgname}
  make install

 # install License
  install -D -m644 LICENSE ${pkgdir}/usr/share/licenses/$pkgname/LICENSE
}
