# Maintainer: Yunhui Fu <yhfudev@gmail.com>
# Contributor: Ken Bull <llubnek@gmail.com>
# Contributor: Todd Musall <tmusall@comcast.net>
# Contributor: tardo <tardo@nagi-fanboi.net>

pkgname=idutils
pkgver=4.6
pkgrel=2
pkgdesc="A package of language independent tools that indexes program identifiers, literal numbers, or words of human-readable text."
arch=('i686' 'x86_64')
url="http://www.gnu.org/software/idutils/"
license=('GPL')
depends=('bash')
replaces=('id-utils')
source=(ftp://ftp.gnu.org/gnu/idutils/idutils-$pkgver.tar.xz)
md5sums=('99b572536377fcddb4d38e86a3c215fd')

build() {
    cd "${srcdir}/$pkgname-$pkgver"
    sed -i -e '/gets is a security/d' lib/stdio.in.h
    sed -i 's/__GNU_LIBRARY__ == 1/__GNU_LIBRARY__ == 1 || defined __GLIBC__/' lib/fseterr.c
    sed -i 's/__GNU_LIBRARY__ == 1/__GNU_LIBRARY__ == 1 || defined __GLIBC__/' lib/fseeko.c
    ./configure --prefix=/usr --disable-gcc-warnings --disable-silent-rules
    #export LC_CTYPE=ISO-8859-1
    make VERBOSE=1 || return 1
}

package () {
    cd "${srcdir}/$pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
    # libuser has lid
    mv $pkgdir/usr/bin/lid $pkgdir/usr/bin/lid-idutils
    mv $pkgdir/usr/share/man/man1/lid.1 $pkgdir/usr/share/man/man1/lid-idutils.1
    # why was this necessary?
    #mkdir -p $pkgdir/usr/share/misc
    #mv $pkgdir/usr/share/id-lang.map $pkgdir/usr/share/misc/
}
