# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=lesstif
pkgver=0.95.2
pkgrel=8
pkgdesc="LGPL'd re-implementation of Motif"
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/lesstif/"
license=('LGPL' 'MIT')
depends=('freetype2' 'libxt' 'libxp')
options=('!makeflags' '!buildflags')
conflicts=('openmotif')
source=("http://downloads.sourceforge.net/${pkgname}/${pkgname}-${pkgver}.tar.bz2"
        'LICENSE'
        '040_fedora_XxxxProperty-64bit.diff')
md5sums=('754187dbac09fcf5d18296437e72a32f'
         'b1f320192a9154f72d83e9d3d5a25a2f'
         '30e2c0babc84696af089d55cb9cb2908')

prepare() {
  cd ${pkgname}-${pkgver}

  # https://bugs.archlinux.org/task/17712
  patch -p1 -i "${srcdir}"/040_fedora_XxxxProperty-64bit.diff
}

build() {
  cd ${pkgname}-${pkgver}

  ./configure --prefix=/usr \
    --enable-production \
    --enable-nonstandard-conversions \
    --enable-editres \
    --with-xdnd \
    --enable-build-21 \
    --disable-debug

  # fix linkage against already installed version
  perl -pi -e 's/^(hardcode_into_libs)=.*/$1=no/' libtool

  make

  # fix linkage against already installed version
  for f in $(find . -name \*.la -type f) ; do
    perl -pi -e 's/^(relink_command=.*)/# $1/' $f
  done

  make -C lib/Mrm-2.1
}

package() {
  cd ${pkgname}-${pkgver}

  make -C lib/Mrm-2.1 DESTDIR="${pkgdir}" install
  make DESTDIR="${pkgdir}" appdir=/usr/share/X11/app-defaults rootdir=/usr/share/doc/LessTif install
  install -Dm644 "${srcdir}"/LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
