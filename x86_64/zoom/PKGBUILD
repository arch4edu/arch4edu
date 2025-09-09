# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>

pkgname=zoom
pkgver=6.5.11.4015
pkgrel=2
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('LicenseRef-zoom')
url="https://zoom.us/"
depends=('fontconfig' 'glib2' 'libpulse' 'libsm' 'ttf-font' 'libx11' 'libxtst' 'libxcb'
	'libxcomposite' 'libxfixes' 'libxi' 'libxcursor' 'libxkbcommon-x11' 'libxrandr'
	'libxrender' 'libxshmfence' 'libxslt' 'mesa' 'nss' 'xcb-util-image'
	'xcb-util-keysyms' 'xcb-util-cursor' 'dbus' 'libdrm' 'gtk3')
optdepends=(
	'ibus: remote control'
	'picom: needed by some window managers for screen sharing'
	)
options=(!strip)
source=("${pkgname}-${pkgver}_orig_x86_64.pkg.tar.xz"::"${url}client/${pkgver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('c150fa1469b9f1bec922a2b47a89a9ebab322427303d37936b364c8b21f2f281debbaa265f52458ea8642df16f49790f8d82fbcbb7c7e947a331f8f91a85e302')

package() {
  mv opt usr "${pkgdir}"
}
