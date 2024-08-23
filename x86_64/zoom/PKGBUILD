# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>

pkgname=zoom
pkgver=6.1.10
_subver=1400
pkgrel=1
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('LicenseRef-zoom')
url="https://zoom.us/"
depends=('fontconfig' 'glib2' 'libpulse' 'libsm' 'ttf-font' 'libx11' 'libxtst' 'libxcb'
	'libxcomposite' 'libxfixes' 'libxi' 'libxcursor' 'libxkbcommon-x11' 'libxrandr'
	'libxrender' 'libxshmfence' 'libxslt' 'mesa' 'nss' 'xcb-util-image'
	'xcb-util-keysyms' 'xcb-util-cursor' 'dbus' 'libdrm' 'gtk3' 'qt5-webengine' 'qt5-remoteobjects')
optdepends=('pulseaudio-alsa: audio via PulseAudio'
	'ibus: remote control'
	'picom: extra compositor needed by some window managers for screen sharing'
	'xcompmgr: extra compositor needed by some window managers for screen sharing')
options=(!strip)
source=("${pkgname}-${pkgver}.${_subver}_orig_x86_64.pkg.tar.xz"::"https://zoom.us/client/${pkgver}.${_subver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('6c2e4eecbf658eb69b222152eeed9a4bab19d6c3c183b80823fc46b332fb752557d4520e0ce65953d268c7a43e35d98492e8786304e5b23e31907c9312b793f7')

prepare() {
	sed -i 's/Zoom\.png/Zoom/g' "${srcdir}/usr/share/applications/Zoom.desktop"
	sed -i 's/StartupWMClass=Zoom/StartupWMClass=zoom/g' "${srcdir}/usr/share/applications/Zoom.desktop"
}

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
