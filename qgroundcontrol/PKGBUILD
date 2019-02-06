# Maintainer: Kye Morton <pryre.dev@outlook.com>
pkgname=qgroundcontrol
pkgver=3.5.0
pkgrel=1
pkgdesc="Ground control for unmanned vehicles."
arch=('any')
url="http://qgroundcontrol.org/"
license=('GPL3')
depends=( 'bzip2' \
		  'dbus' \
		  'flac' \
		  'gst-plugins-base-libs' \
		  'libasyncns' \
		  'libffi' \
		  'libgcrypt' \
		  'libgpg-error' \
		  'libogg' \
		  'libsndfile' \
		  'libsystemd' \
		  'libunwind' \
		  'libx11' \
		  'libxau' \
		  'libxcb' \
		  'libxdmcp' \
		  'libxext' \
		  'lz4' \
		  'orc' \
		  'pcre' \
		  'sdl2' \
		  'xz' \
		  'zlib')

source=('qgroundcontrol-'${pkgver}'-'${pkgrel}'::https://github.com/mavlink/qgroundcontrol/releases/download/v'${pkgver}'/qgroundcontrol.tar.bz2')
sha256sums=('fc2bed2d25a44b2848e7c836779d9cc7746d4c8eb884971b1c5e92699858e1ca')

build() {
  echo "[Desktop Entry]
Type=Application
Name=QGroundControl
Comment=Ground control for unmanned vehicles
Path=/opt/qgroundcontrol/
Exec=/usr/bin/qgroundcontrol
Icon=/opt/qgroundcontrol/qgroundcontrol.png
Terminal=false
Categories=Qt;Utility;" > "$srcdir/${pkgname}/qgroundcontrol.desktop"
}

package() {
  mkdir -p "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/applications"
  cp -R "$srcdir/${pkgname}" "${pkgdir}/opt/qgroundcontrol"
  ln -s "/opt/qgroundcontrol/qgroundcontrol-start.sh" "${pkgdir}/usr/bin/qgroundcontrol"
  ln -s "/opt/qgroundcontrol/qgroundcontrol.desktop" "${pkgdir}/usr/share/applications/qgroundcontrol.desktop"
}

# vim:set ts=2 sw=2 et:
