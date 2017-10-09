# Maintainer: Mike Sampson <mike at sambodata dot com>
# Contributor: Bernhard Walle <bernhard.walle@gmx.de>
# AUR Category: lib
pkgname=libafterimage
pkgver=1.20
pkgrel=2
pkgdesc="Generic image manipulation library"
url="http://www.afterstep.org/afterimage"
license=('GPL')
depends=('libpng' 'libtiff' 'freetype2' 'libxext')
arch=('i686' 'x86_64')
source=(https://downloads.sourceforge.net/project/afterstep/libAfterImage/1.20/libAfterImage-1.20.tar.bz2
        libafterimage-libpng15.patch)
md5sums=('17a0ab8a2e6b253f222934418705963e'
         'bdb49e626cb91b2c218193f3d36c9f91')

build() {
    cd $srcdir/libAfterImage-$pkgver
    # Apply Gentoo's libpng15 patch
    patch < $srcdir/libafterimage-libpng15.patch
    ./configure --prefix=/usr --mandir=/usr/share/man \
                --enable-sharedlibs --disable-staticlibs --without-svg

    # don't run ldconfig
    sed -i -e 's/`uname`/"hack"/g' $srcdir/libAfterImage-$pkgver/Makefile

    make
}

package() {
    cd $srcdir/libAfterImage-$pkgver
    make DESTDIR=$pkgdir install
}

# :mode=shellscript:
