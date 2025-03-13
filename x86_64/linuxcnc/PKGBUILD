# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Gonçalo Pereira
# Contributor: Jason Kercher <jkercher43 a gmail>
# Contributor: Peter Ivanov <ivanovp@gmail.com>
# Contributor: Alec Ari <neotheuser@ymail.com>

pkgname=linuxcnc
pkgver=2.9.4
pkgrel=1
pkgdesc="Controls CNC machines. It can drive milling machines, lathes, 3d printers, laser cutters, plasma cutters, robot arms, hexapods, and more (formerly EMC2)"
arch=(x86_64)
license=(GPL2 'custom: unredestributable')
url="https://linuxcnc.org/"
depends=(glibc python gtk3 libusb libxss python-cairo gobject-introspection-runtime dbus-python python-pillow libxmu
         python-gobject tk python-matplotlib boost-libs python-numpy gstreamer at-spi2-core libepoxy libtirpc libxft
         harfbuzz gcc-libs fontconfig gdk-pixbuf2 libxext librsvg glib2 zlib cairo readline systemd-libs freetype2
         libx11 libxinerama python-configobj libgpiod python-yapps2 tcl pango bwidget)
makedepends=(intltool boost asciidoc glu procps-ng psmisc tclx)
options=(!emptydirs !strip)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/LinuxCNC/linuxcnc/archive/refs/tags/v${pkgver}.tar.gz"
        'unredestributable.txt'
        'libtirpc.patch')
sha256sums=('93aca8d1c602331b17e7b2fefb82318f59c5faef9cacf60514b59cd6bb89be0e'
            '228a035c143ccbdd6056e1189267b034f046742cae034bff821eccc8dbc68ee3'
            'bc95bafd67fad1c1d3722261bc586cdc612ec9e1597fadb95fa825c10550ac2c')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}/src"
  echo "[[ ":\$TCLLIBPATH:" != *":/usr/lib/tcltk/linuxcnc:"* ]] && export TCLLIBPATH="/usr/lib/tcltk/linuxcnc:\$TCLLIBPATH"" > ${pkgname}.sh
  find . -iname fixpaths.py -o -iname checkglade -o \
   -iname update_ini | xargs perl -p -i -e "s/python/python2/"
  patch -Np2 -i $srcdir/libtirpc.patch

  ./autogen.sh

  ./configure \
    --prefix=/usr \
    --enable-non-distributable=yes \
    --with-realtime=uspace \
    --without-libmodbus \
    --disable-gtk2

  # Linking time errors fix
  #sed -i "163s|FileName|FileNameArr|" hal/classicladder/files_project.c
  #sed -i "174s|FileName|FileNameArr|g" hal/classicladder/files_project.c
  #sed -i "175s|FileName|FileNameArr|" hal/classicladder/files_project.c
}

build () {
  cd "${srcdir}/${pkgname}-${pkgver}/src"
  make
}

package() {
  install -Dm644 unredestributable.txt   -t "${pkgdir}"/usr/share/licenses/${pkgname}/
  install -Dm644 "${pkgname}-${pkgver}/src/linuxcnc.sh" -t "${pkgdir}"/etc/profile.d/

  cd "${pkgname}-${pkgver}/src"
  install -Dm644 ../share/menus/CNC.menu -t "${pkgdir}"/etc/xdg/menus/

  DESTDIR="${pkgdir}" make install

  #sed -i "s|${srcdir}||" "${pkgdir}/usr/include/linuxcnc/config.h"
  #sed -i "s|${srcdir}||" "${pkgdir}/usr/share/linuxcnc/Makefile.modinc"


  #cd "${srcdir}/${pkgname}-${pkgver}/src"
  #DESTDIR=${pkgdir} make install
  #cp -PR "${srcdir}/${pkgname}-${pkgver}/share/applications" $pkgdir/usr/share
  #mkdir -p "${pkgdir}/etc/xdg"
  #cp -PR "${srcdir}/${pkgname}-${pkgver}/share/menus" "${pkgdir}/etc/xdg/"
  #install -Dm755 "${srcdir}/${pkgname}-${pkgver}/src/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  #sed -i "s|${srcdir}||" "${pkgdir}/usr/include/linuxcnc/config.h"
  #sed -i "s|${srcdir}||" "${pkgdir}/usr/share/linuxcnc/Makefile.modinc"
  #install -Dm644 "${srcdir}/${pkgname}-${pkgver}/src/linuxcnc.sh" -t "${pkgdir}/etc/profile.d/"
  #install -D -t "${pkgdir}/usr/share/licenses/${pkgname}" "${srcdir}/unredestributable.txt"
}
