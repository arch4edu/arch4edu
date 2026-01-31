# Maintainer: Gonçalo Pereira <you@example.com>
# Contributor: Fabio 'Lolix' Loli <fabio.loli@disroot.org>

pkgname=linuxcnc
pkgver=2.9.8
pkgrel=3
pkgdesc="Controls CNC machines (mills, lathes, 3D printers, robots, etc.)"
arch=(x86_64)
url="https://linuxcnc.org/"
license=(GPL2 custom)
depends=(
  glibc python gtk3 libusb libxss python-cairo gobject-introspection-runtime
  dbus-python python-pillow libxmu python-gobject tk python-matplotlib boost-libs
  python-numpy gstreamer at-spi2-core libepoxy libtirpc libxft harfbuzz fontconfig
  gdk-pixbuf2 libxext librsvg glib2 zlib cairo readline systemd-libs freetype2
  libx11 libxinerama python-configobj libgpiod python-yapps2 tcl pango bwidget
  python-opengl
)
makedepends=(intltool boost asciidoc glu procps-ng psmisc tclx libtirpc)
options=(!strip)

source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/LinuxCNC/linuxcnc/archive/refs/tags/v$pkgver.tar.gz"
  "unredestributable.txt"
)

sha256sums=('e106b0c41b15bb93da7308861b4754ca647d6f4a4f298ed419bf3d192aa4a42f'
            '228a035c143ccbdd6056e1189267b034f046742cae034bff821eccc8dbc68ee3')

prepare() {
  cd "$srcdir/$pkgname-$pkgver/src"

  # libtirpc (glibc no longer provides SunRPC)
  export CPPFLAGS="-I/usr/include/tirpc"
  export CFLAGS="-I/usr/include/tirpc"
  export LDFLAGS="-ltirpc"
  
  ./autogen.sh

  ./configure \
    --prefix=/usr \
    --enable-non-distributable=yes \
    --with-realtime=uspace \
    --without-libmodbus \
    --disable-gtk2
}

build() {
  cd "$srcdir/$pkgname-$pkgver/src"
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver/src"
  DESTDIR="$pkgdir" make install

  # License
  install -Dm644 "$srcdir/unredestributable.txt" \
    "$pkgdir/usr/share/licenses/$pkgname/unredestributable.txt"

  # Desktop menu
  install -Dm644 ../share/menus/CNC.menu \
    "$pkgdir/etc/xdg/menus/CNC.menu"

  # Tcl path fix (TCLLIBPATH is space-separated)
  install -Dm644 /dev/stdin "$pkgdir/etc/profile.d/linuxcnc.sh" <<'EOF'
[[ " $TCLLIBPATH " != *" /usr/lib/tcltk/linuxcnc "* ]] && \
export TCLLIBPATH="/usr/lib/tcltk/linuxcnc $TCLLIBPATH"
EOF

  # Fix Python path (dist-packages → site-packages)
  pyver=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
  if [[ -d "$pkgdir/usr/lib/python3/dist-packages" ]]; then
    mkdir -p "$pkgdir/usr/lib/python$pyver/site-packages"
    mv "$pkgdir/usr/lib/python3/dist-packages/"* "$pkgdir/usr/lib/python$pyver/site-packages/"
    rmdir "$pkgdir/usr/lib/python3/dist-packages" || true
  fi

  # Ensure hallib and modules are in /usr/lib/linuxcnc
  mkdir -p "$pkgdir/usr/lib/linuxcnc/modules"
  cp -a ../rtlib/*.so "$pkgdir/usr/lib/linuxcnc/modules/"

  # Install manpages
  install -Dm644 ../docs/man/man1/*.1 "$pkgdir/usr/share/man/man1"
  install -Dm644 ../docs/man/man3/* "$pkgdir/usr/share/man/man3"
  install -Dm644 ../docs/man/man9/* "$pkgdir/usr/share/man/man9"

  # Fix: Remove /lib directory (Arch uses /usr/lib, /lib is a symlink)
  # Move any contents to /usr/lib if they exist, then remove /lib
  if [[ -d "$pkgdir/lib" ]]; then
    if [[ -n "$(ls -A "$pkgdir/lib")" ]]; then
      cp -a "$pkgdir/lib/"* "$pkgdir/usr/lib/"
    fi
    rm -rf "$pkgdir/lib"
  fi
}
