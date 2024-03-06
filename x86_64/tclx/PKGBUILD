# Maintainer: Peter Ivanov <ivanovp@gmail.com>
# Contributor: Hussain Jasim <hussainmkj@gmail.com>
# Contributors: Flemming Madsen (arch at themadsens dot dk), Sébastien Duquette <ekse.0x@gmail.com>
pkgname=tclx
pkgver=8.6.3
_tclsrcver=8.6.14
pkgrel=1
pkgdesc="Provides OS primitives, file scanning, data records etc. for Tcl"
url="https://github.com/flightaware/tclx"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
license=('BSD')
depends=('tcl=8.6.14' 'tk' 'libtirpc')
source=("https://github.com/flightaware/tclx/archive/refs/tags/v${pkgver}.tar.gz" \
        "http://downloads.sourceforge.net/sourceforge/tcl/tcl${_tclsrcver}-src.tar.gz" \
        "interperrorline.patch")
md5sums=('797dfa26789356e0d2010ea869889fe0'
         'c30b57c6051be28fa928d09aca82841e'
         '3254188674bfa4cdf58605d0d69586d0')

#prepare() {
#  patch -d $srcdir/${pkgname}8.4/generic < interperrorline.patch
#}

build() {
  cd $srcdir/${pkgname}-${pkgver}
  ./configure
  cp /usr/lib/tclConfig.sh $srcdir
  echo "TCL_SRC_DIR=$startdir/tcl$_tclsrcver" >> ../tclConfig.sh
  [ "$NOEXTRACT" == 1 ] || ./configure --prefix=/usr --enable-share \
                           --enable-gcc --with-tcl=$srcdir
  _tclsrc="TCL_SRC_DIR=$srcdir/tcl$_tclsrcver \
           TCL_TOP_DIR_NATIVE=$srcdir/tcl$_tclsrcver"
  CPPFLAGS+=" -I/usr/include/tirpc/"
  LDFLAGS+=" -ltirpc"
  make $_tclsrc || return 1
}

package() {
  cd $srcdir/${pkgname}-${pkgver}
  make $_tclsrc DESTDIR="$pkgdir" mandir="/usr/share/man" install
  install -D -m644 license.terms "$pkgdir/usr/share/licenses/$pkgname/license.terms"
}
