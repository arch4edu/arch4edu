# Maintainer: Kye Morton <pryre.dev@outlook.com>
pkgname=qgroundcontrol
pkgver=3.4.1
pkgrel=1
pkgdesc="Ground control for unmanned vehicles."
arch=('any')
url="http://qgroundcontrol.org/"
license=('GPL3')
depends=(\
  'espeak'  # optional but you have to decide if you want it at built-time\
  'qt5-svg' 'qt5-graphicaleffects' 'qt5-webkit' 'phonon-qt4' 'qt5-serialport'\
  'qt5-quickcontrols')

source=('qgroundcontrol-'${pkgver}'-'${pkgrel}'::https://github.com/mavlink/qgroundcontrol/releases/download/v'${pkgver}'/qgroundcontrol.tar.bz2')
sha256sums=('24d56ec916943c94439bbb55e74af72e352d21f174973ea78c07879a8750284f')

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
