# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Jason Kercher <jkercher43 a gmail>
# Contributor: Peter Ivanov <ivanovp@gmail.com>
# Contributor: Alec Ari <neotheuser@ymail.com>

pkgname=linuxcnc
pkgver=2.9.2
pkgrel=2
pkgdesc="Controls CNC machines. It can drive milling machines, lathes, 3d printers, laser cutters, plasma cutters, robot arms, hexapods, and more (formerly EMC2)"
arch=(x86_64)
license=(GPL2 'custom: unredestributable')
url="https://linuxcnc.org/"
depends=(glibc python gtk3 libusb libxss python-cairo gobject-introspection-runtime dbus-python python-pillow libxmu
         python-gobject tk python-matplotlib boost-libs python-numpy gstreamer at-spi2-core libepoxy libtirpc libxft
         harfbuzz gcc-libs fontconfig gdk-pixbuf2 libxext librsvg glib2 zlib cairo readline systemd-libs freetype2
         libx11 libxinerama python-configobj libgpiod-1.6.4 python-yapps2 tcl pango bwidget)
makedepends=(intltool boost asciidoc glu procps-ng psmisc tclx)
options=(!emptydirs)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/LinuxCNC/linuxcnc/archive/refs/tags/v${pkgver}.tar.gz"
        'unredestributable.txt'
        'libtirpc.patch')
sha256sums=('56648e0a9a6fcd4ea7d5c00174a90177f8e39c2f10b130ceff8f0481f26bfaf7'
            '228a035c143ccbdd6056e1189267b034f046742cae034bff821eccc8dbc68ee3'
            'bc95bafd67fad1c1d3722261bc586cdc612ec9e1597fadb95fa825c10550ac2c')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}/src"
  echo "export TCLLIBPATH=$TCLLIBPATH:/usr/lib/tcltk/linuxcnc" > ${pkgname}.sh
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
  cd "${srcdir}/${pkgname}-${pkgver}/src"
  DESTDIR=${pkgdir} make install
  cp -PR "${srcdir}/${pkgname}-${pkgver}/share/applications" $pkgdir/usr/share
  mkdir -p "${pkgdir}/etc/xdg"
  cp -PR "${srcdir}/${pkgname}-${pkgver}/share/menus" "${pkgdir}/etc/xdg/"
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/src/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  #sed -i "s|${srcdir}||" "${pkgdir}/usr/include/linuxcnc/config.h"
  #sed -i "s|${srcdir}||" "${pkgdir}/usr/share/linuxcnc/Makefile.modinc"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/src/linuxcnc.sh" -t "${pkgdir}/etc/profile.d/"
  install -D -t "${pkgdir}/usr/share/licenses/${pkgname}" "${srcdir}/unredestributable.txt"
}
